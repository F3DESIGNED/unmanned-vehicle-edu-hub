#!/usr/bin/env python3
"""
CTE Research Master Workbook - Phase 2 Builder
Adds OCQ, PDER calculations and PAI helper table infrastructure
"""

import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import get_column_letter
from datetime import datetime
import glob

# Constants
GREEN_FILL = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
LIGHT_GRAY_FILL = PatternFill(start_color="F0F0F0", end_color="F0F0F0", fill_type="solid")
PURPLE_FILL = PatternFill(start_color="E6E6FA", end_color="E6E6FA", fill_type="solid")
HEADER_FILL = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")
BOLD_FONT = Font(bold=True)


def set_tab_color(ws, color_code):
    """Set worksheet tab color"""
    ws.sheet_properties.tabColor = color_code


def create_table(ws, name, ref, headers):
    """Create a formatted Excel table"""
    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Create table
    tab = Table(displayName=name, ref=ref)
    style = TableStyleInfo(
        name="TableStyleMedium2",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=False
    )
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Auto-adjust column widths
    for col_idx in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(col_idx)].width = 20


def add_named_ranges(wb):
    """Add Phase 2 named ranges"""
    print("\n📌 Adding Phase 2 named ranges...")

    new_ranges = {
        "State_Total_Programs": "SUM(tbl_Programs_Fractional[Fractional_Credit])",
        "State_Total_Enrollment": "SUM(tbl_Districts_Clean[Enrollment])",
    }

    for name, formula in new_ranges.items():
        defn = DefinedName(name=name, attr_text=formula)
        wb.defined_names.add(defn)

    print(f"  ✓ Added {len(new_ranges)} named ranges")


def create_ocq_sheet(wb):
    """Sheet 14: OCQ_Calculated"""
    print("\n→ Creating Sheet 14: OCQ_Calculated...")

    # Get district list
    districts_ws = wb["Districts_Clean"]
    districts = []
    for row in range(2, districts_ws.max_row + 1):
        nces_id = districts_ws[f'A{row}'].value
        district_name = districts_ws[f'B{row}'].value
        if nces_id and district_name:
            districts.append((nces_id, district_name))

    # Create sheet
    ws = wb.create_sheet("OCQ_Calculated", 13)  # Insert after Districts_Clean

    headers = ["NCES_ID", "District_Name", "Total_Programs", "StatePathways_Count", "OCQ", "OCQ_Category"]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write data with formulas
    for row_idx, (nces_id, district_name) in enumerate(districts, 2):
        ws[f'A{row_idx}'] = nces_id
        ws[f'B{row_idx}'] = district_name

        # C: Total_Programs
        ws[f'C{row_idx}'] = f'=SUMIFS(tbl_Programs_Fractional[Fractional_Credit],tbl_Programs_Fractional[NCES_ID],A{row_idx})'

        # D: StatePathways_Count (reference named range for transparency)
        ws[f'D{row_idx}'] = '=StatePathways_Count'

        # E: OCQ
        ws[f'E{row_idx}'] = f'=IF(C{row_idx}=0,0,C{row_idx}/D{row_idx}*100)'

        # F: OCQ_Category
        ws[f'F{row_idx}'] = f'=IFS(E{row_idx}=0,"No CTE",E{row_idx}<25,"Limited (<25%)",E{row_idx}<50,"Moderate (25-50%)",E{row_idx}<75,"Substantial (50-75%)",TRUE,"Comprehensive (≥75%)")'

    # Create table
    table_ref = f"A1:F{len(districts) + 1}"
    tab = Table(displayName="tbl_OCQ_Calculated", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Auto-adjust columns
    for col_idx in range(1, 7):
        ws.column_dimensions[get_column_letter(col_idx)].width = 20

    set_tab_color(ws, "90EE90")
    print(f"  ✓ Created OCQ_Calculated with {len(districts)} districts")


def create_pder_sheet(wb):
    """Sheet 20: PDER_Calculated"""
    print("\n→ Creating Sheet 20: PDER_Calculated...")

    # Get district list
    districts_ws = wb["Districts_Clean"]
    districts = []
    for row in range(2, districts_ws.max_row + 1):
        nces_id = districts_ws[f'A{row}'].value
        district_name = districts_ws[f'B{row}'].value
        if nces_id and district_name:
            districts.append((nces_id, district_name))

    # Create sheet at end
    ws = wb.create_sheet("PDER_Calculated")

    headers = ["NCES_ID", "District_Name", "Total_Programs", "District_Enrollment",
               "Program_Share", "Enrollment_Share", "PDER", "PDER_Interpretation"]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write data with formulas
    for row_idx, (nces_id, district_name) in enumerate(districts, 2):
        ws[f'A{row_idx}'] = nces_id
        ws[f'B{row_idx}'] = district_name

        # C: Total_Programs
        ws[f'C{row_idx}'] = f'=SUMIFS(tbl_Programs_Fractional[Fractional_Credit],tbl_Programs_Fractional[NCES_ID],A{row_idx})'

        # D: District_Enrollment
        ws[f'D{row_idx}'] = f'=IFERROR(INDEX(tbl_Districts_Clean[Enrollment],MATCH(A{row_idx},tbl_Districts_Clean[NCES_ID],0)),0)'

        # E: Program_Share
        ws[f'E{row_idx}'] = f'=IF(State_Total_Programs=0,0,C{row_idx}/State_Total_Programs)'

        # F: Enrollment_Share
        ws[f'F{row_idx}'] = f'=IF(State_Total_Enrollment=0,0,D{row_idx}/State_Total_Enrollment)'

        # G: PDER
        ws[f'G{row_idx}'] = f'=IF(F{row_idx}=0,0,E{row_idx}/F{row_idx})'

        # H: PDER_Interpretation
        ws[f'H{row_idx}'] = f'=IFS(G{row_idx}=0,"No Programs",G{row_idx}<0.5,"Severely Under-Represented",G{row_idx}<0.8,"Under-Represented",G{row_idx}<=1.2,"Equitable",G{row_idx}<=2.0,"Over-Represented",TRUE,"Highly Over-Represented")'

    # Create table
    table_ref = f"A1:H{len(districts) + 1}"
    tab = Table(displayName="tbl_PDER_Calculated", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Auto-adjust columns
    for col_idx in range(1, 9):
        ws.column_dimensions[get_column_letter(col_idx)].width = 22

    set_tab_color(ws, "90EE90")
    print(f"  ✓ Created PDER_Calculated with {len(districts)} districts")


def create_helper_county(wb):
    """Helper_Alignment_County - FULL IMPLEMENTATION"""
    print("\n→ Creating Helper_Alignment_County (complete)...")

    # Get all district-program combinations
    programs_ws = wb["Programs_Fractional"]
    district_programs = []
    for row in range(2, programs_ws.max_row + 1):
        nces_id = programs_ws[f'A{row}'].value
        cip_code = programs_ws[f'B{row}'].value
        program_name = programs_ws[f'D{row}'].value
        if nces_id and cip_code:
            district_programs.append((nces_id, cip_code, program_name))

    # Create sheet after OCQ_Calculated
    ws = wb.create_sheet("Helper_Alignment_County", 14)

    headers = [
        "NCES_ID", "District_Name", "County", "CIP_Code", "Program_Name", "SOC_Code",
        "Occupation_Title", "Median_Wage", "Regional_Median_Wage", "Annual_Openings_Current",
        "Annual_Openings_10yr", "Wage_Ratio", "Is_High_Wage_110", "Is_High_Wage_120",
        "Is_High_Wage_130", "Rank_Current", "Rank_10yr", "Is_Top15_Current", "Is_Top20_Current",
        "Is_Top15_10yr", "Is_Top20_10yr", "Aligned_110_Top15_Current", "Aligned_110_Top15_10yr",
        "Aligned_110_Top20_Current", "Aligned_110_Top20_10yr", "Aligned_120_Top15_Current",
        "Aligned_120_Top15_10yr", "Aligned_120_Top20_Current", "Aligned_120_Top20_10yr",
        "Aligned_130_Top15_Current", "Aligned_130_Top15_10yr", "Aligned_130_Top20_Current",
        "Aligned_130_Top20_10yr"
    ]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write data with formulas
    for row_idx, (nces_id, cip_code, program_name) in enumerate(district_programs, 2):
        # A: NCES_ID
        ws[f'A{row_idx}'] = nces_id

        # B: District_Name
        ws[f'B{row_idx}'] = f'=IFERROR(INDEX(tbl_Districts_Clean[District_Name],MATCH(A{row_idx},tbl_Districts_Clean[NCES_ID],0)),"")'

        # C: County
        ws[f'C{row_idx}'] = f'=IFERROR(INDEX(tbl_Districts_Clean[County],MATCH(A{row_idx},tbl_Districts_Clean[NCES_ID],0)),"")'

        # D: CIP_Code
        ws[f'D{row_idx}'] = cip_code

        # E: Program_Name
        ws[f'E{row_idx}'] = program_name

        # F: SOC_Code
        ws[f'F{row_idx}'] = f'=IFERROR(INDEX(tbl_CIP_SOC_Crosswalk[SOC_Code],MATCH(D{row_idx},tbl_CIP_SOC_Crosswalk[CIP_Code],0)),"")'

        # G: Occupation_Title
        ws[f'G{row_idx}'] = f'=IFERROR(INDEX(tbl_CIP_SOC_Crosswalk[Pathway_Name],MATCH(D{row_idx},tbl_CIP_SOC_Crosswalk[CIP_Code],0)),"")'

        # H: Median_Wage (lookup from Labor_Market_County using county + SOC)
        ws[f'H{row_idx}'] = f'=IFERROR(SUMIFS(tbl_Labor_County[Median_Wage],tbl_Labor_County[County],C{row_idx},tbl_Labor_County[SOC_Code],F{row_idx}),0)'

        # I: Regional_Median_Wage
        ws[f'I{row_idx}'] = f'=IFERROR(SUMIFS(tbl_Labor_County[Regional_Median_Wage],tbl_Labor_County[County],C{row_idx},tbl_Labor_County[SOC_Code],F{row_idx}),0)'

        # J: Annual_Openings_Current
        ws[f'J{row_idx}'] = f'=IFERROR(SUMIFS(tbl_Labor_County[Annual_Openings_Current],tbl_Labor_County[County],C{row_idx},tbl_Labor_County[SOC_Code],F{row_idx}),0)'

        # K: Annual_Openings_10yr
        ws[f'K{row_idx}'] = f'=IFERROR(SUMIFS(tbl_Labor_County[Annual_Openings_10yr],tbl_Labor_County[County],C{row_idx},tbl_Labor_County[SOC_Code],F{row_idx}),0)'

        # L: Wage_Ratio
        ws[f'L{row_idx}'] = f'=IF(I{row_idx}=0,0,H{row_idx}/I{row_idx})'

        # M: Is_High_Wage_110
        ws[f'M{row_idx}'] = f'=IF(L{row_idx}>=1.10,"Yes","No")'

        # N: Is_High_Wage_120
        ws[f'N{row_idx}'] = f'=IF(L{row_idx}>=1.20,"Yes","No")'

        # O: Is_High_Wage_130
        ws[f'O{row_idx}'] = f'=IF(L{row_idx}>=1.30,"Yes","No")'

        # P: Rank_Current (using COUNTIFS to rank within county)
        ws[f'P{row_idx}'] = f'=IF(J{row_idx}=0,999,COUNTIFS(tbl_Labor_County[County],C{row_idx},tbl_Labor_County[Annual_Openings_Current],">"&J{row_idx})+1)'

        # Q: Rank_10yr
        ws[f'Q{row_idx}'] = f'=IF(K{row_idx}=0,999,COUNTIFS(tbl_Labor_County[County],C{row_idx},tbl_Labor_County[Annual_Openings_10yr],">"&K{row_idx})+1)'

        # R: Is_Top15_Current
        ws[f'R{row_idx}'] = f'=IF(P{row_idx}<=15,"Yes","No")'

        # S: Is_Top20_Current
        ws[f'S{row_idx}'] = f'=IF(P{row_idx}<=20,"Yes","No")'

        # T: Is_Top15_10yr
        ws[f'T{row_idx}'] = f'=IF(Q{row_idx}<=15,"Yes","No")'

        # U: Is_Top20_10yr
        ws[f'U{row_idx}'] = f'=IF(Q{row_idx}<=20,"Yes","No")'

        # V-AG: Alignment flags (12 combinations)
        # Aligned_110_Top15_Current
        ws[f'V{row_idx}'] = f'=IF(AND(M{row_idx}="Yes",R{row_idx}="Yes"),"Yes","No")'
        # Aligned_110_Top15_10yr
        ws[f'W{row_idx}'] = f'=IF(AND(M{row_idx}="Yes",T{row_idx}="Yes"),"Yes","No")'
        # Aligned_110_Top20_Current
        ws[f'X{row_idx}'] = f'=IF(AND(M{row_idx}="Yes",S{row_idx}="Yes"),"Yes","No")'
        # Aligned_110_Top20_10yr
        ws[f'Y{row_idx}'] = f'=IF(AND(M{row_idx}="Yes",U{row_idx}="Yes"),"Yes","No")'
        # Aligned_120_Top15_Current
        ws[f'Z{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",R{row_idx}="Yes"),"Yes","No")'
        # Aligned_120_Top15_10yr
        ws[f'AA{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",T{row_idx}="Yes"),"Yes","No")'
        # Aligned_120_Top20_Current
        ws[f'AB{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",S{row_idx}="Yes"),"Yes","No")'
        # Aligned_120_Top20_10yr
        ws[f'AC{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",U{row_idx}="Yes"),"Yes","No")'
        # Aligned_130_Top15_Current
        ws[f'AD{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",R{row_idx}="Yes"),"Yes","No")'
        # Aligned_130_Top15_10yr
        ws[f'AE{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",T{row_idx}="Yes"),"Yes","No")'
        # Aligned_130_Top20_Current
        ws[f'AF{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",S{row_idx}="Yes"),"Yes","No")'
        # Aligned_130_Top20_10yr
        ws[f'AG{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",U{row_idx}="Yes"),"Yes","No")'

    # Create table
    table_ref = f"A1:AG{len(district_programs) + 1}"
    tab = Table(displayName="tbl_Helper_County", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Auto-adjust columns
    for col_idx in range(1, 34):
        ws.column_dimensions[get_column_letter(col_idx)].width = 18

    set_tab_color(ws, "F0F0F0")
    print(f"  ✓ Created Helper_Alignment_County with {len(district_programs)} rows (32 columns)")


def create_helper_templates(wb):
    """Create template shells for H2-H5"""
    print("\n→ Creating helper table templates (H2-H5)...")

    helper_configs = [
        ("Helper_Alignment_CEPD", "CEPD_Region", "tbl_Helper_CEPD"),
        ("Helper_Alignment_Prosperity", "Prosperity_Region", "tbl_Helper_Prosperity"),
        ("Helper_Alignment_Metropolitan", "Metropolitan_Region", "tbl_Helper_Metropolitan"),
        ("Helper_Alignment_Economic", "Economic_Region", "tbl_Helper_Economic"),
    ]

    headers = [
        "NCES_ID", "District_Name", "Region", "CIP_Code", "Program_Name", "SOC_Code",
        "Occupation_Title", "Median_Wage", "Regional_Median_Wage", "Annual_Openings_Current",
        "Annual_Openings_10yr", "Wage_Ratio", "Is_High_Wage_110", "Is_High_Wage_120",
        "Is_High_Wage_130", "Rank_Current", "Rank_10yr", "Is_Top15_Current", "Is_Top20_Current",
        "Is_Top15_10yr", "Is_Top20_10yr", "Aligned_110_Top15_Current", "Aligned_110_Top15_10yr",
        "Aligned_110_Top20_Current", "Aligned_110_Top20_10yr", "Aligned_120_Top15_Current",
        "Aligned_120_Top15_10yr", "Aligned_120_Top20_Current", "Aligned_120_Top20_10yr",
        "Aligned_130_Top15_Current", "Aligned_130_Top15_10yr", "Aligned_130_Top20_Current",
        "Aligned_130_Top20_10yr"
    ]

    for sheet_name, region_col, table_name in helper_configs:
        ws = wb.create_sheet(sheet_name)

        # Write headers only
        for col_idx, header in enumerate(headers, 1):
            cell = ws.cell(row=1, column=col_idx, value=header)
            cell.font = HEADER_FONT
            cell.fill = HEADER_FILL

        # Add note in row 2
        ws['A2'] = "TEMPLATE: Full implementation in Phase 3"
        ws['A2'].font = Font(italic=True, color="808080")

        # Auto-adjust columns
        for col_idx in range(1, 34):
            ws.column_dimensions[get_column_letter(col_idx)].width = 18

        set_tab_color(ws, "F0F0F0")

    print(f"  ✓ Created {len(helper_configs)} helper templates")


def update_variable_codebook(wb):
    """Add Phase 2 variables to codebook"""
    print("\n→ Updating Variable_Codebook...")

    ws = wb["Variable_Codebook"]

    # Find last row
    last_row = ws.max_row

    # New variables for Phase 2
    new_variables = [
        ["OCQ", "Decimal", "0-100", "Opportunity Coverage Quotient - % of state pathways accessible", "OCQ_Calculated", "Calculated"],
        ["OCQ_Category", "Text", "5 categories", "Categorical interpretation of OCQ", "OCQ_Calculated", "IFS formula"],
        ["Total_Programs", "Decimal", ">=0", "Sum of fractional credits for district", "Multiple sheets", "SUMIFS"],
        ["PDER", "Decimal", ">=0", "Program Distribution Equity Ratio", "PDER_Calculated", "Calculated"],
        ["Program_Share", "Decimal", "0-1", "District's share of total state programs", "PDER_Calculated", "Division"],
        ["Enrollment_Share", "Decimal", "0-1", "District's share of total state enrollment", "PDER_Calculated", "Division"],
        ["PDER_Interpretation", "Text", "6 categories", "Categorical equity assessment", "PDER_Calculated", "IFS formula"],
        ["Wage_Ratio", "Decimal", ">=0", "Occupation wage relative to regional median", "Helper tables", "Division"],
        ["Is_High_Wage_110", "Text", "Yes/No", "Wage >= 110% of regional median", "Helper tables", "IF formula"],
        ["Is_High_Wage_120", "Text", "Yes/No", "Wage >= 120% of regional median", "Helper tables", "IF formula"],
        ["Is_High_Wage_130", "Text", "Yes/No", "Wage >= 130% of regional median", "Helper tables", "IF formula"],
        ["Rank_Current", "Integer", ">=1", "Occupation rank by current openings within region", "Helper tables", "COUNTIFS"],
        ["Rank_10yr", "Integer", ">=1", "Occupation rank by 10-year openings within region", "Helper tables", "COUNTIFS"],
        ["Is_Top15_Current", "Text", "Yes/No", "Occupation in top 15 by current openings", "Helper tables", "IF formula"],
        ["Is_Top20_Current", "Text", "Yes/No", "Occupation in top 20 by current openings", "Helper tables", "IF formula"],
        ["Aligned_[Config]", "Text", "Yes/No", "Program aligned under specific configuration (12 variants)", "Helper tables", "AND formula"],
    ]

    for idx, var_data in enumerate(new_variables, last_row + 1):
        for col_idx, value in enumerate(var_data, 1):
            ws.cell(row=idx, column=col_idx, value=value)

    print(f"  ✓ Added {len(new_variables)} new variable definitions")


def update_formula_key(wb):
    """Add Phase 2 formulas to formula key"""
    print("\n→ Updating Formula_Key...")

    ws = wb["Formula_Key"]

    # Find last row
    last_row = ws.max_row

    # New formulas for Phase 2
    new_formulas = [
        ["OCQ", "OCQ_Calculated, Column E", "=IF([@Total_Programs]=0,0,[@Total_Programs]/[@StatePathways_Count]*100)", "If district has no programs return 0; otherwise divide total programs by state pathways and multiply by 100 to get percentage", "25 programs ÷ 50 pathways = 50%"],
        ["OCQ_Category", "OCQ_Calculated, Column F", '=IFS([@OCQ]=0,"No CTE",[@OCQ]<25,"Limited (<25%)",[...5 conditions])', "Categorizes OCQ into 5 tiers based on coverage level", "OCQ=35% → Moderate (25-50%)"],
        ["PDER", "PDER_Calculated, Column G", "=IF([@Enrollment_Share]=0,0,[@Program_Share]/[@Enrollment_Share])", "Divides program share by enrollment share; 1.0 = equity, <1.0 = underserved, >1.0 = overserved", "Prog 2%, Enroll 1% → PDER=2.0"],
        ["Program_Share", "PDER_Calculated, Column E", "=IF(State_Total_Programs=0,0,[@Total_Programs]/State_Total_Programs)", "District's programs divided by total state programs", "5 programs ÷ 100 state total = 5%"],
        ["State_Total_Programs", "Named Range", "=SUM(tbl_Programs_Fractional[Fractional_Credit])", "Sum of all fractional credits across all districts", "Used in PDER calculations"],
        ["State_Total_Enrollment", "Named Range", "=SUM(tbl_Districts_Clean[Enrollment])", "Total enrollment across all districts", "Used in PDER calculations"],
        ["Wage_Ratio", "Helper tables, Column L", "=IF([@Regional_Median_Wage]=0,0,[@Median_Wage]/[@Regional_Median_Wage])", "Occupation median wage divided by regional median wage", "$54K wage ÷ $45K regional = 1.20"],
        ["Rank_Current", "Helper tables, Column P", '=IF([@Annual_Openings_Current]=0,999,COUNTIFS(tbl_Labor_County[County],[@County],tbl_Labor_County[Annual_Openings_Current],">"&[@Annual_Openings_Current])+1)', "Counts how many occupations in same region have MORE openings, then adds 1 for rank", "3 occupations with more openings → Rank 4"],
        ["Aligned_120_Top15_Current", "Helper tables, Column Z", '=IF(AND([@Is_High_Wage_120]="Yes",[@Is_Top15_Current]="Yes"),"Yes","No")', "Returns Yes only if occupation meets BOTH wage threshold (120%) AND rank threshold (Top 15) for current period", "High wage + Rank 12 → Aligned"],
        ["Helper Table Logic", "Multiple columns", "[32-column structure]", "Helper tables pre-calculate all alignment flags to make PAI formulas simple SUMIFS operations instead of nested lookups", "See full helper documentation"],
    ]

    for idx, formula_data in enumerate(new_formulas, last_row + 1):
        for col_idx, value in enumerate(formula_data, 1):
            ws.cell(row=idx, column=col_idx, value=value)

    print(f"  ✓ Added {len(new_formulas)} new formula explanations")


def main():
    """Main execution function"""
    print("=" * 60)
    print("CTE RESEARCH MASTER WORKBOOK - PHASE 2 BUILDER")
    print("=" * 60)

    # Load Phase 1 workbook
    wb_files = glob.glob("CTE_Research_Master_Phase1_*.xlsx")
    if not wb_files:
        print("\n✗ ERROR: Phase 1 workbook not found!")
        return None

    wb_path = wb_files[0]
    print(f"\n📂 Loading Phase 1 workbook: {wb_path}")

    try:
        wb = load_workbook(wb_path)
        print(f"✓ Workbook loaded successfully")
        print(f"✓ Phase 1 sheets: {len(wb.sheetnames)}")
    except Exception as e:
        print(f"\n✗ ERROR: Could not load workbook: {e}")
        return None

    # Add Phase 2 components
    print("\n" + "=" * 60)
    print("ADDING PHASE 2 COMPONENTS")
    print("=" * 60)

    add_named_ranges(wb)
    create_ocq_sheet(wb)
    create_pder_sheet(wb)
    create_helper_county(wb)
    create_helper_templates(wb)
    update_variable_codebook(wb)
    update_formula_key(wb)

    # Save workbook
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"CTE_Research_Master_Phase2_{timestamp}.xlsx"
    wb.save(filename)

    print("\n" + "=" * 60)
    print(f"✅ Phase 2 workbook created: {filename}")
    print(f"   Total sheets: {len(wb.sheetnames)}")
    print(f"   Named ranges: {len(wb.defined_names)}")
    print("=" * 60 + "\n")

    return filename


if __name__ == "__main__":
    main()
