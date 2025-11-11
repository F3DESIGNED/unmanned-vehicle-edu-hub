#!/usr/bin/env python3
"""
CTE Research Master Workbook - Phase 3 Builder
Completes PAI calculations, Master Analysis Table, and validation infrastructure
"""

import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from datetime import datetime
import glob

# Constants
GREEN_FILL = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
LIGHT_GRAY_FILL = PatternFill(start_color="F0F0F0", end_color="F0F0F0", fill_type="solid")
ORANGE_FILL = PatternFill(start_color="FFB366", end_color="FFB366", fill_type="solid")
WHITE_FILL = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
HEADER_FILL = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")
BOLD_FONT = Font(bold=True)


def set_tab_color(ws, color_code):
    """Set worksheet tab color"""
    ws.sheet_properties.tabColor = color_code


def update_helper_county_fractional(wb):
    """Add Fractional_Credit column to Helper_Alignment_County"""
    print("\n→ Updating Helper_Alignment_County with Fractional_Credit...")

    ws = wb["Helper_Alignment_County"]

    # Insert new column after Program_Name (column E)
    ws.insert_cols(6)  # Insert at column F

    # Update header
    ws['F1'] = "Fractional_Credit"
    ws['F1'].font = HEADER_FONT
    ws['F1'].fill = HEADER_FILL

    # Add formula for each row
    for row in range(2, ws.max_row + 1):
        # Lookup fractional credit from Programs_Fractional
        ws[f'F{row}'] = f'=IFERROR(SUMIFS(tbl_Programs_Fractional[Fractional_Credit],tbl_Programs_Fractional[NCES_ID],A{row},tbl_Programs_Fractional[CIP_Code],D{row}),0)'

    # Update table reference to include new column
    old_table = ws.tables["tbl_Helper_County"]
    new_ref = f"A1:AH{ws.max_row}"  # Was AG, now AH with new column
    old_table.ref = new_ref

    print(f"  ✓ Added Fractional_Credit column to Helper_Alignment_County")


def build_helper_table(wb, sheet_name, region_col_name, region_table_col, labor_table_name, table_name):
    """Build a complete helper table for a geographic level"""
    print(f"\n→ Building {sheet_name}...")

    # Get district-program combinations
    programs_ws = wb["Programs_Fractional"]
    district_programs = []
    for row in range(2, programs_ws.max_row + 1):
        nces_id = programs_ws[f'A{row}'].value
        cip_code = programs_ws[f'B{row}'].value
        program_name = programs_ws[f'D{row}'].value
        if nces_id and cip_code:
            district_programs.append((nces_id, cip_code, program_name))

    # Get or create sheet
    if sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        # Clear existing data (keep headers)
        ws.delete_rows(2, ws.max_row)
    else:
        ws = wb.create_sheet(sheet_name)

    headers = [
        "NCES_ID", "District_Name", region_col_name, "CIP_Code", "Program_Name",
        "Fractional_Credit", "SOC_Code", "Occupation_Title", "Median_Wage",
        "Regional_Median_Wage", "Annual_Openings_Current", "Annual_Openings_10yr",
        "Wage_Ratio", "Is_High_Wage_110", "Is_High_Wage_120", "Is_High_Wage_130",
        "Rank_Current", "Rank_10yr", "Is_Top15_Current", "Is_Top20_Current",
        "Is_Top15_10yr", "Is_Top20_10yr", "Aligned_110_Top15_Current",
        "Aligned_110_Top15_10yr", "Aligned_110_Top20_Current", "Aligned_110_Top20_10yr",
        "Aligned_120_Top15_Current", "Aligned_120_Top15_10yr", "Aligned_120_Top20_Current",
        "Aligned_120_Top20_10yr", "Aligned_130_Top15_Current", "Aligned_130_Top15_10yr",
        "Aligned_130_Top20_Current", "Aligned_130_Top20_10yr"
    ]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write formulas for each district-program
    for row_idx, (nces_id, cip_code, program_name) in enumerate(district_programs, 2):
        ws[f'A{row_idx}'] = nces_id
        ws[f'B{row_idx}'] = f'=IFERROR(INDEX(tbl_Districts_Clean[District_Name],MATCH(A{row_idx},tbl_Districts_Clean[NCES_ID],0)),"")'
        ws[f'C{row_idx}'] = f'=IFERROR(INDEX(tbl_Districts_Clean[{region_table_col}],MATCH(A{row_idx},tbl_Districts_Clean[NCES_ID],0)),"")'
        ws[f'D{row_idx}'] = cip_code
        ws[f'E{row_idx}'] = program_name
        ws[f'F{row_idx}'] = f'=IFERROR(SUMIFS(tbl_Programs_Fractional[Fractional_Credit],tbl_Programs_Fractional[NCES_ID],A{row_idx},tbl_Programs_Fractional[CIP_Code],D{row_idx}),0)'
        ws[f'G{row_idx}'] = f'=IFERROR(INDEX(tbl_CIP_SOC_Crosswalk[SOC_Code],MATCH(D{row_idx},tbl_CIP_SOC_Crosswalk[CIP_Code],0)),"")'
        ws[f'H{row_idx}'] = f'=IFERROR(INDEX(tbl_CIP_SOC_Crosswalk[Pathway_Name],MATCH(D{row_idx},tbl_CIP_SOC_Crosswalk[CIP_Code],0)),"")'
        ws[f'I{row_idx}'] = f'=IFERROR(SUMIFS({labor_table_name}[Median_Wage],{labor_table_name}[{region_col_name}],C{row_idx},{labor_table_name}[SOC_Code],G{row_idx}),0)'
        ws[f'J{row_idx}'] = f'=IFERROR(SUMIFS({labor_table_name}[Regional_Median_Wage],{labor_table_name}[{region_col_name}],C{row_idx},{labor_table_name}[SOC_Code],G{row_idx}),0)'
        ws[f'K{row_idx}'] = f'=IFERROR(SUMIFS({labor_table_name}[Annual_Openings_Current],{labor_table_name}[{region_col_name}],C{row_idx},{labor_table_name}[SOC_Code],G{row_idx}),0)'
        ws[f'L{row_idx}'] = f'=IFERROR(SUMIFS({labor_table_name}[Annual_Openings_10yr],{labor_table_name}[{region_col_name}],C{row_idx},{labor_table_name}[SOC_Code],G{row_idx}),0)'
        ws[f'M{row_idx}'] = f'=IF(J{row_idx}=0,0,I{row_idx}/J{row_idx})'
        ws[f'N{row_idx}'] = f'=IF(M{row_idx}>=1.10,"Yes","No")'
        ws[f'O{row_idx}'] = f'=IF(M{row_idx}>=1.20,"Yes","No")'
        ws[f'P{row_idx}'] = f'=IF(M{row_idx}>=1.30,"Yes","No")'
        ws[f'Q{row_idx}'] = f'=IF(K{row_idx}=0,999,COUNTIFS({labor_table_name}[{region_col_name}],C{row_idx},{labor_table_name}[Annual_Openings_Current],">"&K{row_idx})+1)'
        ws[f'R{row_idx}'] = f'=IF(L{row_idx}=0,999,COUNTIFS({labor_table_name}[{region_col_name}],C{row_idx},{labor_table_name}[Annual_Openings_10yr],">"&L{row_idx})+1)'
        ws[f'S{row_idx}'] = f'=IF(Q{row_idx}<=15,"Yes","No")'
        ws[f'T{row_idx}'] = f'=IF(Q{row_idx}<=20,"Yes","No")'
        ws[f'U{row_idx}'] = f'=IF(R{row_idx}<=15,"Yes","No")'
        ws[f'V{row_idx}'] = f'=IF(R{row_idx}<=20,"Yes","No")'
        # Alignment flags
        ws[f'W{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",S{row_idx}="Yes"),"Yes","No")'
        ws[f'X{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",U{row_idx}="Yes"),"Yes","No")'
        ws[f'Y{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",T{row_idx}="Yes"),"Yes","No")'
        ws[f'Z{row_idx}'] = f'=IF(AND(N{row_idx}="Yes",V{row_idx}="Yes"),"Yes","No")'
        ws[f'AA{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",S{row_idx}="Yes"),"Yes","No")'
        ws[f'AB{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",U{row_idx}="Yes"),"Yes","No")'
        ws[f'AC{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",T{row_idx}="Yes"),"Yes","No")'
        ws[f'AD{row_idx}'] = f'=IF(AND(O{row_idx}="Yes",V{row_idx}="Yes"),"Yes","No")'
        ws[f'AE{row_idx}'] = f'=IF(AND(P{row_idx}="Yes",S{row_idx}="Yes"),"Yes","No")'
        ws[f'AF{row_idx}'] = f'=IF(AND(P{row_idx}="Yes",U{row_idx}="Yes"),"Yes","No")'
        ws[f'AG{row_idx}'] = f'=IF(AND(P{row_idx}="Yes",T{row_idx}="Yes"),"Yes","No")'
        ws[f'AH{row_idx}'] = f'=IF(AND(P{row_idx}="Yes",V{row_idx}="Yes"),"Yes","No")'

    # Create/update table
    table_ref = f"A1:AH{len(district_programs) + 1}"
    if table_name in ws.tables:
        ws.tables[table_name].ref = table_ref
    else:
        tab = Table(displayName=table_name, ref=table_ref)
        style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                              showLastColumn=False, showRowStripes=True, showColumnStripes=False)
        tab.tableStyleInfo = style
        ws.add_table(tab)

    # Adjust columns
    for col_idx in range(1, 35):
        ws.column_dimensions[get_column_letter(col_idx)].width = 18

    set_tab_color(ws, "F0F0F0")
    print(f"  ✓ Built {sheet_name} with {len(district_programs)} rows")


def build_pai_sheet(wb, sheet_name, region_col, helper_table_name, table_name, sheet_index=None):
    """Build a PAI calculation sheet for a geographic level"""
    print(f"\n→ Building {sheet_name}...")

    # Get district list
    districts_ws = wb["Districts_Clean"]
    districts = []
    for row in range(2, districts_ws.max_row + 1):
        nces_id = districts_ws[f'A{row}'].value
        district_name = districts_ws[f'B{row}'].value
        if nces_id and district_name:
            districts.append((nces_id, district_name))

    # Create sheet
    if sheet_index is not None:
        ws = wb.create_sheet(sheet_name, sheet_index)
    else:
        ws = wb.create_sheet(sheet_name)

    # Headers - 17 columns total
    base_headers = ["NCES_ID", "District_Name"]
    if region_col != "County":  # County already in Districts_Clean
        base_headers.append(region_col)

    headers = base_headers + [
        "Total_Programs",
        "Aligned_110_Top15_Current", "Aligned_110_Top15_10yr",
        "Aligned_110_Top20_Current", "Aligned_110_Top20_10yr",
        "Aligned_120_Top15_Current", "Aligned_120_Top15_10yr",
        "Aligned_120_Top20_Current", "Aligned_120_Top20_10yr",
        "Aligned_130_Top15_Current", "Aligned_130_Top15_10yr",
        "Aligned_130_Top20_Current", "Aligned_130_Top20_10yr",
        "PAI_Active_Config", "PAI_Category"
    ]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    col_offset = len(base_headers)

    # Write formulas
    for row_idx, (nces_id, district_name) in enumerate(districts, 2):
        ws[f'A{row_idx}'] = nces_id
        ws[f'B{row_idx}'] = district_name

        if region_col != "County":
            # Add region lookup
            ws[f'C{row_idx}'] = f'=IFERROR(INDEX(tbl_Districts_Clean[{region_col}],MATCH(A{row_idx},tbl_Districts_Clean[NCES_ID],0)),"")'

        # Total_Programs
        total_col = get_column_letter(col_offset + 1)
        ws[f'{total_col}{row_idx}'] = f'=SUMIFS(tbl_Programs_Fractional[Fractional_Credit],tbl_Programs_Fractional[NCES_ID],A{row_idx})'

        # 12 aligned program counts
        alignment_configs = [
            "Aligned_110_Top15_Current", "Aligned_110_Top15_10yr",
            "Aligned_110_Top20_Current", "Aligned_110_Top20_10yr",
            "Aligned_120_Top15_Current", "Aligned_120_Top15_10yr",
            "Aligned_120_Top20_Current", "Aligned_120_Top20_10yr",
            "Aligned_130_Top15_Current", "Aligned_130_Top15_10yr",
            "Aligned_130_Top20_Current", "Aligned_130_Top20_10yr"
        ]

        for idx, config in enumerate(alignment_configs):
            col = get_column_letter(col_offset + 2 + idx)
            ws[f'{col}{row_idx}'] = f'=SUMIFS({helper_table_name}[Fractional_Credit],{helper_table_name}[NCES_ID],A{row_idx},{helper_table_name}[{config}],"Yes")'

        # PAI_Active_Config (using nested IFs - simpler than CHOOSE)
        pai_col = get_column_letter(col_offset + 14)
        aligned_cols = [get_column_letter(col_offset + 2 + i) for i in range(12)]

        ws[f'{pai_col}{row_idx}'] = f'''=IF({total_col}{row_idx}=0,0,
IF(AND(Active_Toggle_Wage="110%",Active_Toggle_OccCount="Top 15",Active_Toggle_TimeRef="Current"),{aligned_cols[0]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="110%",Active_Toggle_OccCount="Top 15",Active_Toggle_TimeRef="10-Year Projection"),{aligned_cols[1]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="110%",Active_Toggle_OccCount="Top 20",Active_Toggle_TimeRef="Current"),{aligned_cols[2]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="110%",Active_Toggle_OccCount="Top 20",Active_Toggle_TimeRef="10-Year Projection"),{aligned_cols[3]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="120%",Active_Toggle_OccCount="Top 15",Active_Toggle_TimeRef="Current"),{aligned_cols[4]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="120%",Active_Toggle_OccCount="Top 15",Active_Toggle_TimeRef="10-Year Projection"),{aligned_cols[5]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="120%",Active_Toggle_OccCount="Top 20",Active_Toggle_TimeRef="Current"),{aligned_cols[6]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="120%",Active_Toggle_OccCount="Top 20",Active_Toggle_TimeRef="10-Year Projection"),{aligned_cols[7]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="130%",Active_Toggle_OccCount="Top 15",Active_Toggle_TimeRef="Current"),{aligned_cols[8]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="130%",Active_Toggle_OccCount="Top 15",Active_Toggle_TimeRef="10-Year Projection"),{aligned_cols[9]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="130%",Active_Toggle_OccCount="Top 20",Active_Toggle_TimeRef="Current"),{aligned_cols[10]}{row_idx}/{total_col}{row_idx}*100,
IF(AND(Active_Toggle_Wage="130%",Active_Toggle_OccCount="Top 20",Active_Toggle_TimeRef="10-Year Projection"),{aligned_cols[11]}{row_idx}/{total_col}{row_idx}*100,
0)))))))))))))'''

        # PAI_Category
        cat_col = get_column_letter(col_offset + 15)
        ws[f'{cat_col}{row_idx}'] = f'=IFS({pai_col}{row_idx}=0,"No Alignment",{pai_col}{row_idx}<25,"Low (<25%)",{pai_col}{row_idx}<50,"Moderate (25-50%)",{pai_col}{row_idx}<75,"Good (50-75%)",TRUE,"Excellent (≥75%)")'

    # Create table
    end_col = get_column_letter(col_offset + 15)
    table_ref = f"A1:{end_col}{len(districts) + 1}"
    tab = Table(displayName=table_name, ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                          showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Adjust columns
    for col_idx in range(1, col_offset + 16):
        ws.column_dimensions[get_column_letter(col_idx)].width = 20

    set_tab_color(ws, "90EE90")
    print(f"  ✓ Built {sheet_name} with {len(districts)} districts")


def build_master_analysis_table(wb):
    """Build the comprehensive Master_Analysis_Table"""
    print("\n→ Building Master_Analysis_Table (60+ columns)...")

    # Get district list
    districts_ws = wb["Districts_Clean"]
    districts = []
    for row in range(2, districts_ws.max_row + 1):
        nces_id = districts_ws[f'A{row}'].value
        if nces_id:
            districts.append(nces_id)

    ws = wb.create_sheet("Master_Analysis_Table")

    # Define all 60+ headers
    headers = [
        # Section 1: Identifiers
        "NCES_ID", "District_Name", "County",
        # Section 2: Geographic Classifications
        "Locale_Code", "Locale_Category", "Locale_Label", "CEPD_Region",
        "Prosperity_Region", "Metropolitan_Region", "Economic_Region",
        "Is_City", "Is_Suburb", "Is_Town", "Is_Rural",
        # Section 3: District Characteristics
        "Enrollment", "FRL_Count", "FRL_Percent", "Perkins_Funding",
        "Unemployment_Rate", "District_Wealth_Index",
        # Section 4: Program Availability
        "Has_CTE", "Total_Programs", "OCQ", "OCQ_Category",
        # Section 5: PAI - All 5 Geographic Levels
        "PAI_County", "PAI_County_Category", "PAI_CEPD", "PAI_CEPD_Category",
        "PAI_Prosperity", "PAI_Prosperity_Category", "PAI_Metropolitan",
        "PAI_Metropolitan_Category", "PAI_Economic", "PAI_Economic_Category",
        # Section 6: Equity
        "PDER", "PDER_Interpretation",
        # Section 7: Toggle Configuration
        "Config_District_Inclusion", "Config_Wage_Threshold",
        "Config_Occupation_Count", "Config_Time_Reference",
        # Section 8: Analysis Inclusion
        "Include_In_Analysis",
        # Section 9: Standardized Variables
        "Z_Enrollment", "Z_FRL_Percent", "Z_Perkins_Funding",
        "Z_Unemployment_Rate", "Z_District_Wealth", "Z_OCQ",
        # Section 10: Derived Binary Variables
        "Has_High_FRL", "Has_Low_Wealth", "Has_High_Unemployment",
        "OCQ_High", "OCQ_Low", "PAI_County_High", "PAI_County_Low",
        "PDER_Equitable", "PDER_UnderRep", "PDER_OverRep"
    ]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write formulas for each district
    for row_idx, nces_id in enumerate(districts, 2):
        col = 1

        # Section 1: Identifiers
        ws.cell(row=row_idx, column=col, value=nces_id); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[District_Name],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[County],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1

        # Section 2: Geographic Classifications
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Locale_Code],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Locale_Category],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Locale_Label],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[CEPD_Region],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Prosperity_Region],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Metropolitan_Region],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Economic_Region],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        # Binary locale flags (use column letter references)
        locale_cat_col = get_column_letter(5)
        ws.cell(row=row_idx, column=col, value=f'=IF({locale_cat_col}{row_idx}="City",1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({locale_cat_col}{row_idx}="Suburb",1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({locale_cat_col}{row_idx}="Town",1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({locale_cat_col}{row_idx}="Rural",1,0)'); col += 1

        # Section 3: District Characteristics
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Enrollment],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[FRL_Count],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[FRL_Percent],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_Control_Variables[Perkins_Funding],MATCH($A{row_idx},tbl_Control_Variables[NCES_ID],0)),0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_Control_Variables[Unemployment_Rate],MATCH($A{row_idx},tbl_Control_Variables[NCES_ID],0)),0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_Control_Variables[District_Wealth_Index],MATCH($A{row_idx},tbl_Control_Variables[NCES_ID],0)),0)'); col += 1

        # Section 4: Program Availability
        ws.cell(row=row_idx, column=col, value=f'=INDEX(tbl_Districts_Clean[Has_CTE],MATCH($A{row_idx},tbl_Districts_Clean[NCES_ID],0))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_OCQ_Calculated[Total_Programs],MATCH($A{row_idx},tbl_OCQ_Calculated[NCES_ID],0)),0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_OCQ_Calculated[OCQ],MATCH($A{row_idx},tbl_OCQ_Calculated[NCES_ID],0)),0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_OCQ_Calculated[OCQ_Category],MATCH($A{row_idx},tbl_OCQ_Calculated[NCES_ID],0)),"")'); col += 1

        # Section 5: PAI - 5 Geographic Levels (2 columns each)
        pai_tables = [
            ("tbl_PAI_County", "PAI_Active_Config", "PAI_Category"),
            ("tbl_PAI_CEPD", "PAI_Active_Config", "PAI_Category"),
            ("tbl_PAI_Prosperity", "PAI_Active_Config", "PAI_Category"),
            ("tbl_PAI_Metropolitan", "PAI_Active_Config", "PAI_Category"),
            ("tbl_PAI_Economic", "PAI_Active_Config", "PAI_Category")
        ]
        for tbl_name, pai_col, cat_col_name in pai_tables:
            ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX({tbl_name}[{pai_col}],MATCH($A{row_idx},{tbl_name}[NCES_ID],0)),0)'); col += 1
            ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX({tbl_name}[{cat_col_name}],MATCH($A{row_idx},{tbl_name}[NCES_ID],0)),"")'); col += 1

        # Section 6: Equity
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_PDER_Calculated[PDER],MATCH($A{row_idx},tbl_PDER_Calculated[NCES_ID],0)),0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IFERROR(INDEX(tbl_PDER_Calculated[PDER_Interpretation],MATCH($A{row_idx},tbl_PDER_Calculated[NCES_ID],0)),"")'); col += 1

        # Section 7: Toggle Configuration (record current settings)
        ws.cell(row=row_idx, column=col, value='=Active_Toggle_District'); col += 1
        ws.cell(row=row_idx, column=col, value='=Active_Toggle_Wage'); col += 1
        ws.cell(row=row_idx, column=col, value='=Active_Toggle_OccCount'); col += 1
        ws.cell(row=row_idx, column=col, value='=Active_Toggle_TimeRef'); col += 1

        # Section 8: Analysis Inclusion
        has_cte_col = get_column_letter(21)
        ws.cell(row=row_idx, column=col, value=f'=IF(Active_Toggle_District="All Districts","Yes",IF({has_cte_col}{row_idx}="Yes","Yes","No"))'); col += 1

        # Section 9: Standardized Variables (Z-scores)
        include_col = get_column_letter(col - 1)
        enrollment_col = get_column_letter(15)
        frl_pct_col = get_column_letter(17)
        perkins_col = get_column_letter(18)
        unemp_col = get_column_letter(19)
        wealth_col = get_column_letter(20)
        ocq_col = get_column_letter(23)

        # Z_Enrollment
        ws.cell(row=row_idx, column=col, value=f'=IF({include_col}{row_idx}="No",NA(),({enrollment_col}{row_idx}-AVERAGEIF({include_col}:{include_col},"Yes",{enrollment_col}:{enrollment_col}))/STDEV(IF({include_col}:{include_col}="Yes",{enrollment_col}:{enrollment_col})))'); col += 1
        # Z_FRL_Percent
        ws.cell(row=row_idx, column=col, value=f'=IF({include_col}{row_idx}="No",NA(),({frl_pct_col}{row_idx}-AVERAGEIF({include_col}:{include_col},"Yes",{frl_pct_col}:{frl_pct_col}))/STDEV(IF({include_col}:{include_col}="Yes",{frl_pct_col}:{frl_pct_col})))'); col += 1
        # Simplified for other Z-scores - use AVERAGE and STDEV.S
        ws.cell(row=row_idx, column=col, value=f'=IF({include_col}{row_idx}="No",NA(),({perkins_col}{row_idx}-AVERAGE({perkins_col}:{perkins_col}))/STDEV.S({perkins_col}:{perkins_col}))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({include_col}{row_idx}="No",NA(),({unemp_col}{row_idx}-AVERAGE({unemp_col}:{unemp_col}))/STDEV.S({unemp_col}:{unemp_col}))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({include_col}{row_idx}="No",NA(),({wealth_col}{row_idx}-AVERAGE({wealth_col}:{wealth_col}))/STDEV.S({wealth_col}:{wealth_col}))'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({include_col}{row_idx}="No",NA(),({ocq_col}{row_idx}-AVERAGE({ocq_col}:{ocq_col}))/STDEV.S({ocq_col}:{ocq_col}))'); col += 1

        # Section 10: Derived Binary Variables
        ws.cell(row=row_idx, column=col, value=f'=IF({frl_pct_col}{row_idx}>=50,1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({wealth_col}{row_idx}<1,1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({unemp_col}{row_idx}>6,1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({ocq_col}{row_idx}>=MEDIAN({ocq_col}:{ocq_col}),1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({ocq_col}{row_idx}<MEDIAN({ocq_col}:{ocq_col}),1,0)'); col += 1
        pai_county_col = get_column_letter(25)
        ws.cell(row=row_idx, column=col, value=f'=IF({pai_county_col}{row_idx}>=MEDIAN({pai_county_col}:{pai_county_col}),1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({pai_county_col}{row_idx}<MEDIAN({pai_county_col}:{pai_county_col}),1,0)'); col += 1
        pder_col = get_column_letter(35)
        ws.cell(row=row_idx, column=col, value=f'=IF(AND({pder_col}{row_idx}>=0.8,{pder_col}{row_idx}<=1.2),1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({pder_col}{row_idx}<0.8,1,0)'); col += 1
        ws.cell(row=row_idx, column=col, value=f'=IF({pder_col}{row_idx}>1.2,1,0)'); col += 1

    # Create table
    end_col = get_column_letter(len(headers))
    table_ref = f"A1:{end_col}{len(districts) + 1}"
    tab = Table(displayName="tbl_Master_Analysis", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False,
                          showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Adjust columns
    for col_idx in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(col_idx)].width = 18

    set_tab_color(ws, "FFFFFF")
    print(f"  ✓ Built Master_Analysis_Table with {len(headers)} columns, {len(districts)} rows")


def build_quick_validation_sheet(wb):
    """Build automated validation check sheet"""
    print("\n→ Building Quick_Validation sheet...")

    ws = wb.create_sheet("Quick_Validation")

    # Title
    ws['A1'] = "WORKBOOK VALIDATION REPORT"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:C1')

    # Section headers and checks
    checks = [
        ("", "", ""),
        ("DATA INTEGRITY CHECKS", "", ""),
        ("All districts have NCES_ID", '=IF(COUNTBLANK(tbl_Districts_Clean[NCES_ID])=0,"✓ PASS","✗ FAIL - Blank IDs found")', ""),
        ("All districts have Locale_Code", '=IF(COUNTBLANK(tbl_Districts_Clean[Locale_Code])=0,"✓ PASS","✗ FAIL - Blank codes")', ""),
        ("No duplicate NCES_IDs", '=IF(SUMPRODUCT(1/COUNTIF(tbl_Districts_Clean[NCES_ID],tbl_Districts_Clean[NCES_ID]))=COUNTA(tbl_Districts_Clean[NCES_ID]),"✓ PASS","✗ FAIL - Duplicates")', ""),
        ("All Enrollments > 0", '=IF(COUNTIF(tbl_Districts_Clean[Enrollment],"<=0")=0,"✓ PASS","✗ FAIL - Invalid enrollment")', ""),
        ("", "", ""),
        ("METRIC RANGE CHECKS", "", ""),
        ("OCQ within 0-100%", '=IF(AND(MIN(tbl_OCQ_Calculated[OCQ])>=0,MAX(tbl_OCQ_Calculated[OCQ])<=100),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("PAI_County within 0-100%", '=IF(AND(MIN(tbl_PAI_County[PAI_Active_Config])>=0,MAX(tbl_PAI_County[PAI_Active_Config])<=100),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("PAI_CEPD within 0-100%", '=IF(AND(MIN(tbl_PAI_CEPD[PAI_Active_Config])>=0,MAX(tbl_PAI_CEPD[PAI_Active_Config])<=100),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("PAI_Prosperity within 0-100%", '=IF(AND(MIN(tbl_PAI_Prosperity[PAI_Active_Config])>=0,MAX(tbl_PAI_Prosperity[PAI_Active_Config])<=100),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("PAI_Metropolitan within 0-100%", '=IF(AND(MIN(tbl_PAI_Metropolitan[PAI_Active_Config])>=0,MAX(tbl_PAI_Metropolitan[PAI_Active_Config])<=100),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("PAI_Economic within 0-100%", '=IF(AND(MIN(tbl_PAI_Economic[PAI_Active_Config])>=0,MAX(tbl_PAI_Economic[PAI_Active_Config])<=100),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("PDER within reasonable range", '=IF(AND(MIN(tbl_PDER_Calculated[PDER])>=0,MAX(tbl_PDER_Calculated[PDER])<=10),"✓ PASS","✗ FAIL - Out of range")', ""),
        ("", "", ""),
        ("CALCULATION CHECKS", "", ""),
        ("State_Total_Programs > 0", '=IF(State_Total_Programs>0,"✓ PASS","✗ FAIL - Invalid total")', ""),
        ("State_Total_Enrollment > 0", '=IF(State_Total_Enrollment>0,"✓ PASS","✗ FAIL - Invalid total")', ""),
        ("Program_Share sums to ~100%", '=IF(ABS(SUM(tbl_PDER_Calculated[Program_Share])-1)<0.01,"✓ PASS","✗ FAIL - Doesn\'t sum to 1")', ""),
        ("Enrollment_Share sums to ~100%", '=IF(ABS(SUM(tbl_PDER_Calculated[Enrollment_Share])-1)<0.01,"✓ PASS","✗ FAIL - Doesn\'t sum to 1")', ""),
        ("", "", ""),
        ("TOGGLE FUNCTIONALITY", "", ""),
        ("Toggle dropdowns operational", "[Manual check]", "[User verifies]"),
        ("PAI updates with toggle changes", "[Manual check]", "[User verifies]"),
        ("", "", ""),
        ("OVERALL STATUS", "", ""),
        ('=IF(COUNTIFS(B:B,"✗*")=0,"✓✓ READY FOR EXPORT TO R","✗ ISSUES DETECTED - REVIEW ABOVE")', "", ""),
    ]

    for row_idx, (check, formula, note) in enumerate(checks, 1):
        ws[f'A{row_idx}'] = check
        if formula:
            ws[f'B{row_idx}'] = formula
        if note:
            ws[f'C{row_idx}'] = note

        # Bold section headers
        if check and formula == "":
            ws[f'A{row_idx}'].font = BOLD_FONT

    # Column widths
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 20

    # Add note about manual checks
    ws['A28'] = "Note: Manual checks require user verification after workbook is opened"
    ws['A28'].font = Font(italic=True)

    set_tab_color(ws, "FFB366")
    print(f"  ✓ Built Quick_Validation with automated checks")


def main():
    """Main execution"""
    print("=" * 60)
    print("CTE RESEARCH MASTER WORKBOOK - PHASE 3 BUILDER")
    print("=" * 60)

    # Load Phase 2 workbook
    wb_files = glob.glob("CTE_Research_Master_Phase2_*.xlsx")
    if not wb_files:
        print("\n✗ ERROR: Phase 2 workbook not found!")
        return None

    wb_path = wb_files[0]
    print(f"\n📂 Loading Phase 2 workbook: {wb_path}")

    try:
        wb = load_workbook(wb_path)
        print(f"✓ Workbook loaded successfully")
        print(f"✓ Phase 2 sheets: {len(wb.sheetnames)}")
    except Exception as e:
        print(f"\n✗ ERROR: Could not load workbook: {e}")
        return None

    print("\n" + "=" * 60)
    print("PHASE 3 IMPLEMENTATION")
    print("=" * 60)

    # Step 1: Update Helper_Alignment_County
    update_helper_county_fractional(wb)

    # Step 2: Build H2-H5
    build_helper_table(wb, "Helper_Alignment_CEPD", "CEPD_Region", "CEPD_Region",
                      "tbl_Labor_CEPD", "tbl_Helper_CEPD")
    build_helper_table(wb, "Helper_Alignment_Prosperity", "Prosperity_Region", "Prosperity_Region",
                      "tbl_Labor_Prosperity", "tbl_Helper_Prosperity")
    build_helper_table(wb, "Helper_Alignment_Metropolitan", "Metropolitan_Region", "Metropolitan_Region",
                      "tbl_Labor_Metropolitan", "tbl_Helper_Metropolitan")
    build_helper_table(wb, "Helper_Alignment_Economic", "Economic_Region", "Economic_Region",
                      "tbl_Labor_Economic", "tbl_Helper_Economic")

    # Step 3: Build PAI sheets
    # Find correct insertion points (after helpers, before PDER)
    build_pai_sheet(wb, "PAI_County", "County", "tbl_Helper_County", "tbl_PAI_County")
    build_pai_sheet(wb, "PAI_CEPD", "CEPD_Region", "tbl_Helper_CEPD", "tbl_PAI_CEPD")
    build_pai_sheet(wb, "PAI_Prosperity", "Prosperity_Region", "tbl_Helper_Prosperity", "tbl_PAI_Prosperity")
    build_pai_sheet(wb, "PAI_Metropolitan", "Metropolitan_Region", "tbl_Helper_Metropolitan", "tbl_PAI_Metropolitan")
    build_pai_sheet(wb, "PAI_Economic", "Economic_Region", "tbl_Helper_Economic", "tbl_PAI_Economic")

    # Step 4: Build Master_Analysis_Table
    build_master_analysis_table(wb)

    # Step 5: Build Quick_Validation
    build_quick_validation_sheet(wb)

    # Save workbook
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"CTE_Research_Master_v1.0_{timestamp}.xlsx"

    print("\n" + "=" * 60)
    print("SAVING WORKBOOK...")
    print("=" * 60)

    wb.save(filename)

    print(f"\n✅ Phase 3 workbook created: {filename}")
    print(f"   Total sheets: {len(wb.sheetnames)}")
    print(f"   Named ranges: {len(wb.defined_names)}")
    print("\n" + "=" * 60)

    return filename


if __name__ == "__main__":
    main()
