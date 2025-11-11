#!/usr/bin/env python3
"""
CTE Research Master Workbook - Phase 1 Builder
Creates foundation architecture with all raw data sheets, parameters, and basic processing sheets.
"""

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import get_column_letter
from datetime import datetime
import random

# Constants
ORANGE_FILL = PatternFill(start_color="FFB366", end_color="FFB366", fill_type="solid")
GRAY_FILL = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")
BLUE_FILL = PatternFill(start_color="ADD8E6", end_color="ADD8E6", fill_type="solid")
YELLOW_FILL = PatternFill(start_color="FFFF99", end_color="FFFF99", fill_type="solid")
PURPLE_FILL = PatternFill(start_color="E6E6FA", end_color="E6E6FA", fill_type="solid")
BOLD_FONT = Font(bold=True)
HEADER_FILL = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
HEADER_FONT = Font(bold=True, color="FFFFFF")

# Sample data
DISTRICTS_DATA = [
    ["2600010", "Detroit Public Schools", "Wayne", 11, 45000, 35000, 77.8],
    ["2600020", "Ann Arbor Public Schools", "Washtenaw", 21, 17000, 3400, 20.0],
    ["2601234", "Traverse City Area PS", "Grand Traverse", 22, 10500, 4200, 40.0],
    ["2605678", "Frankenmuth School District", "Saginaw", 32, 1200, 240, 20.0],
    ["2609876", "Onaway Area Community SD", "Presque Isle", 43, 650, 390, 60.0],
    ["2602345", "Grand Rapids Public Schools", "Kent", 11, 19000, 12000, 63.2],
    ["2603456", "Novi Community Schools", "Oakland", 21, 6500, 800, 12.3],
    ["2604567", "East Lansing Public Schools", "Ingham", 21, 3200, 640, 20.0],
    ["2606789", "Petoskey Public Schools", "Emmet", 32, 2100, 840, 40.0],
    ["2607890", "Manistique Area Schools", "Schoolcraft", 42, 890, 445, 50.0],
    ["2608901", "Ironwood Area Schools", "Gogebic", 43, 720, 504, 70.0],
    ["2600234", "Livonia Public Schools", "Wayne", 21, 14500, 4350, 30.0],
    ["2601345", "Midland Public Schools", "Midland", 22, 7800, 2340, 30.0],
]

PROGRAMS_DATA = [
    ["2600010", "47.0201", "26000100", "Heating, AC & Refrigeration", "Active"],
    ["2600010", "52.0201", "26000101", "Business Administration", "Active"],
    ["2600010", "11.0201", "26000102", "Computer Programming", "Active"],
    ["2600020", "11.0201", "26000200", "Computer Programming", "Active"],
    ["2600020", "47.0201", "81050100", "HVAC (ISD Shared)", "Active"],
    ["2600020", "51.0801", "26000201", "Medical Assistant", "Active"],
    ["2601234", "47.0201", "81050100", "HVAC (ISD Shared)", "Active"],
    ["2601234", "51.0911", "26012300", "Massage Therapy", "Active"],
    ["2601234", "52.0201", "26012301", "Business Management", "Active"],
    ["2605678", "01.0101", "26056780", "Agricultural Business", "Active"],
    ["2605678", "47.0201", "81050100", "HVAC (ISD Shared)", "Active"],
    ["2609876", "01.0101", "26098760", "Agricultural Science", "Active"],
    ["2609876", "47.0605", "81050200", "Welding (ISD Shared)", "Active"],
    ["2602345", "47.0201", "26023450", "HVAC Technology", "Active"],
    ["2602345", "52.0201", "26023451", "Business & Marketing", "Active"],
    ["2602345", "51.0801", "26023452", "Health Occupations", "Active"],
    ["2602345", "11.0201", "26023453", "Information Technology", "Active"],
    ["2603456", "11.0201", "26034560", "Computer Science", "Active"],
    ["2603456", "52.0201", "26034561", "Business Analytics", "Active"],
    ["2604567", "51.0801", "26045670", "Medical Careers", "Active"],
    ["2604567", "47.0201", "81050100", "HVAC (ISD Shared)", "Active"],
    ["2606789", "01.0101", "26067890", "Agriculture & Natural Resources", "Active"],
    ["2606789", "47.0605", "81050200", "Welding (ISD Shared)", "Active"],
    ["2607890", "47.0605", "81050200", "Welding (ISD Shared)", "Active"],
    ["2607890", "47.0201", "26078900", "Building Trades", "Active"],
    ["2608901", "01.0101", "26089010", "Natural Resources", "Active"],
    ["2608901", "47.0605", "26089011", "Manufacturing Technology", "Active"],
    ["2600234", "51.0801", "26002340", "Health Sciences", "Active"],
    ["2600234", "11.0201", "26002341", "IT & Cybersecurity", "Active"],
    ["2601345", "52.0201", "26013450", "Business Technology", "Active"],
    ["2601345", "47.0201", "26013451", "Engineering & Trades", "Active"],
]

CIP_SOC_DATA = [
    ["47.0201", "49-9021", "HVAC Mechanics and Installers"],
    ["52.0201", "11-3021", "Business Operations Specialists"],
    ["11.0201", "15-1251", "Computer Programmers"],
    ["51.0911", "31-9011", "Massage Therapists"],
    ["01.0101", "11-9013", "Farmers, Ranchers, and Agricultural Managers"],
    ["51.0801", "31-9092", "Medical Assistants"],
    ["47.0605", "51-4121", "Welders, Cutters, and Welder Fitters"],
]

GEOGRAPHIC_CROSSWALK_DATA = [
    ["Wayne", "Southeast", "Detroit Metro", "Detroit-Warren-Dearborn", "Southeast Michigan"],
    ["Washtenaw", "Southeast", "Ann Arbor Area", "Ann Arbor", "Southeast Michigan"],
    ["Grand Traverse", "Northwest", "Traverse City Area", "Not Metropolitan", "Northern Michigan"],
    ["Saginaw", "East Central", "Saginaw-Midland-Bay City", "Saginaw", "East Michigan"],
    ["Presque Isle", "Northeast", "Rural Northeast", "Not Metropolitan", "Northern Michigan"],
    ["Kent", "West", "Grand Rapids Metro", "Grand Rapids-Wyoming", "West Michigan"],
    ["Oakland", "Southeast", "Detroit Metro", "Detroit-Warren-Dearborn", "Southeast Michigan"],
    ["Ingham", "Central", "Lansing Area", "Lansing-East Lansing", "Central Michigan"],
    ["Emmet", "Northwest", "Northern Lakeshore", "Not Metropolitan", "Northern Michigan"],
    ["Schoolcraft", "Upper Peninsula", "Central UP", "Not Metropolitan", "Upper Peninsula"],
    ["Gogebic", "Upper Peninsula", "Western UP", "Not Metropolitan", "Upper Peninsula"],
    ["Midland", "East Central", "Saginaw-Midland-Bay City", "Midland", "East Michigan"],
]


def create_table(ws, name, ref, data, headers):
    """Create a formatted Excel table"""
    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write data
    for row_idx, row_data in enumerate(data, 2):
        for col_idx, value in enumerate(row_data, 1):
            ws.cell(row=row_idx, column=col_idx, value=value)

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
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column].width = adjusted_width


def set_tab_color(ws, color_code):
    """Set worksheet tab color"""
    ws.sheet_properties.tabColor = color_code


def create_parameters_sheet(wb):
    """Sheet 00: Parameters"""
    ws = wb.create_sheet("Parameters", 0)

    # Headers
    ws['A1'] = "Parameter_Name"
    ws['B1'] = "Value"
    ws['C1'] = "Description"

    # Data
    params = [
        ["StatePathways_Count", 50, "Total Michigan CTE pathways (user updates)"],
        ["Wage_Threshold_110", 1.10, "110% of regional median"],
        ["Wage_Threshold_120", 1.20, "120% of regional median"],
        ["Wage_Threshold_130", 1.30, "130% of regional median"],
        ["Top_Occupation_15", 15, "Top 15 occupations by openings"],
        ["Top_Occupation_20", 20, "Top 20 occupations by openings"],
    ]

    for idx, row in enumerate(params, 2):
        ws[f'A{idx}'] = row[0]
        ws[f'B{idx}'] = row[1]
        ws[f'C{idx}'] = row[2]

    # Format header
    for cell in ws[1]:
        cell.font = BOLD_FONT
        cell.fill = ORANGE_FILL

    # Auto-adjust columns
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 50

    set_tab_color(ws, "FFB366")
    ws.sheet_state = 'hidden'

    return ws


def create_districts_raw_sheet(wb):
    """Sheet 01: Districts_Raw"""
    ws = wb.create_sheet("Districts_Raw")

    headers = ["NCES_ID", "District_Name", "County", "Locale_Code", "Enrollment", "FRL_Count", "FRL_Percent"]
    table_ref = f"A1:G{len(DISTRICTS_DATA) + 1}"

    create_table(ws, "tbl_Districts_Raw", table_ref, DISTRICTS_DATA, headers)
    set_tab_color(ws, "D3D3D3")

    # Protection
    ws.protection.password = "CTE2025"
    ws.protection.sheet = True

    return ws


def create_programs_raw_sheet(wb):
    """Sheet 02: Programs_Raw"""
    ws = wb.create_sheet("Programs_Raw")

    headers = ["NCES_ID", "CIP_Code", "Building_Code", "Program_Name", "Program_Status"]
    table_ref = f"A1:E{len(PROGRAMS_DATA) + 1}"

    create_table(ws, "tbl_Programs_Raw", table_ref, PROGRAMS_DATA, headers)
    set_tab_color(ws, "D3D3D3")

    # Protection
    ws.protection.password = "CTE2025"
    ws.protection.sheet = True

    return ws


def create_labor_market_sheets(wb):
    """Sheets 03-07: Labor_Market data"""

    counties = ["Wayne", "Washtenaw", "Grand Traverse", "Saginaw", "Presque Isle", "Kent", "Oakland", "Ingham", "Emmet", "Schoolcraft", "Gogebic", "Midland"]
    soc_codes = [
        ["49-9021", "HVAC Mechanics and Installers"],
        ["11-3021", "Computer and Information Systems Managers"],
        ["15-1251", "Computer Programmers"],
        ["31-9011", "Massage Therapists"],
        ["11-9013", "Farmers, Ranchers, and Agricultural Managers"],
        ["31-9092", "Medical Assistants"],
        ["51-4121", "Welders, Cutters, Solderers, and Brazers"],
        ["29-1141", "Registered Nurses"],
        ["41-3031", "Securities and Commodities Traders"],
        ["47-2031", "Carpenters"],
    ]

    # Regional median wages by county
    regional_medians = {
        "Wayne": 45000, "Washtenaw": 48000, "Grand Traverse": 42000,
        "Saginaw": 41000, "Presque Isle": 38000, "Kent": 46000,
        "Oakland": 52000, "Ingham": 44000, "Emmet": 41000,
        "Schoolcraft": 39000, "Gogebic": 38000, "Midland": 47000
    }

    # Sheet 03: County level
    ws_county = wb.create_sheet("Labor_Market_County")
    headers_county = ["County", "SOC_Code", "Occupation_Title", "Median_Wage", "Regional_Median_Wage", "Annual_Openings_Current", "Annual_Openings_10yr"]

    data_county = []
    for county in counties:
        regional_median = regional_medians[county]
        for soc, title in soc_codes:
            wage_multiplier = random.uniform(0.85, 1.65)
            median_wage = int(regional_median * wage_multiplier)

            # Scale openings by county size
            base_openings = 50 if county in ["Wayne", "Oakland", "Kent"] else 25 if county in ["Washtenaw", "Ingham", "Saginaw"] else 15
            current_openings = int(base_openings * random.uniform(0.7, 1.3))
            future_openings = int(current_openings * random.uniform(1.05, 1.25))

            data_county.append([county, soc, title, median_wage, regional_median, current_openings, future_openings])

    table_ref = f"A1:G{len(data_county) + 1}"
    create_table(ws_county, "tbl_Labor_County", table_ref, data_county, headers_county)
    set_tab_color(ws_county, "D3D3D3")

    # Sheets 04-07: Regional variants (simplified - same structure, different region column)
    regions_config = [
        ("Labor_Market_CEPD", "CEPD_Region", "tbl_Labor_CEPD", ["Southeast", "Northwest", "East Central", "Northeast", "West", "Central", "Upper Peninsula"]),
        ("Labor_Market_Prosperity", "Prosperity_Region", "tbl_Labor_Prosperity", ["Detroit Metro", "Ann Arbor Area", "Grand Rapids Metro", "Traverse City Area", "Rural Northeast", "Central UP"]),
        ("Labor_Market_Metropolitan", "Metropolitan_Region", "tbl_Labor_Metropolitan", ["Detroit-Warren-Dearborn", "Ann Arbor", "Grand Rapids-Wyoming", "Not Metropolitan"]),
        ("Labor_Market_Economic", "Economic_Region", "tbl_Labor_Economic", ["Southeast Michigan", "West Michigan", "Northern Michigan", "East Michigan", "Central Michigan", "Upper Peninsula"]),
    ]

    for sheet_name, region_col, table_name, region_list in regions_config:
        ws = wb.create_sheet(sheet_name)
        headers = [region_col, "SOC_Code", "Occupation_Title", "Median_Wage", "Regional_Median_Wage", "Annual_Openings_Current", "Annual_Openings_10yr"]

        data = []
        for region in region_list:
            regional_median = random.choice([40000, 43000, 46000, 49000])
            for soc, title in soc_codes[:8]:  # Use subset
                median_wage = int(regional_median * random.uniform(0.9, 1.5))
                current_openings = int(random.uniform(30, 150))
                future_openings = int(current_openings * random.uniform(1.05, 1.2))
                data.append([region, soc, title, median_wage, regional_median, current_openings, future_openings])

        table_ref = f"A1:G{len(data) + 1}"
        create_table(ws, table_name, table_ref, data, headers)
        set_tab_color(ws, "D3D3D3")


def create_cip_soc_crosswalk_sheet(wb):
    """Sheet 08: CIP_SOC_Crosswalk"""
    ws = wb.create_sheet("CIP_SOC_Crosswalk")

    headers = ["CIP_Code", "SOC_Code", "Pathway_Name"]
    table_ref = f"A1:C{len(CIP_SOC_DATA) + 1}"

    create_table(ws, "tbl_CIP_SOC_Crosswalk", table_ref, CIP_SOC_DATA, headers)
    set_tab_color(ws, "D3D3D3")

    return ws


def create_geographic_crosswalk_sheet(wb):
    """Sheet 09: Geographic_Crosswalk"""
    ws = wb.create_sheet("Geographic_Crosswalk")

    headers = ["County", "CEPD_Region", "Prosperity_Region", "Metropolitan_Region", "Economic_Region"]
    table_ref = f"A1:E{len(GEOGRAPHIC_CROSSWALK_DATA) + 1}"

    create_table(ws, "tbl_Geographic_Crosswalk", table_ref, GEOGRAPHIC_CROSSWALK_DATA, headers)
    set_tab_color(ws, "D3D3D3")

    return ws


def create_control_variables_sheet(wb):
    """Sheet 10: Control_Variables_Raw"""
    ws = wb.create_sheet("Control_Variables_Raw")

    headers = ["NCES_ID", "Perkins_Funding", "Unemployment_Rate", "District_Wealth_Index", "Urbanicity_Score"]

    data = []
    for district in DISTRICTS_DATA:
        nces_id = district[0]
        enrollment = district[4]

        # Scale funding by enrollment
        perkins = int(enrollment * random.uniform(15, 35))
        unemployment = round(random.uniform(3.0, 9.0), 1)
        wealth = round(random.uniform(0.6, 2.0), 2)

        # Urbanicity correlates with locale code
        locale_code = district[3]
        urbanicity = 95 if locale_code <= 13 else 75 if locale_code <= 23 else 55 if locale_code <= 33 else 35
        urbanicity += random.randint(-5, 5)

        data.append([nces_id, perkins, unemployment, wealth, urbanicity])

    table_ref = f"A1:E{len(data) + 1}"
    create_table(ws, "tbl_Control_Variables", table_ref, data, headers)
    set_tab_color(ws, "D3D3D3")

    return ws


def create_districts_clean_sheet(wb):
    """Sheet 11: Districts_Clean with formulas"""
    ws = wb.create_sheet("Districts_Clean")

    headers = ["NCES_ID", "District_Name", "County", "Locale_Code", "Locale_Category",
               "Locale_Label", "Enrollment", "FRL_Count", "FRL_Percent", "Has_CTE",
               "CEPD_Region", "Prosperity_Region", "Metropolitan_Region", "Economic_Region"]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write data with formulas
    for row_idx, district in enumerate(DISTRICTS_DATA, 2):
        ws[f'A{row_idx}'] = district[0]  # NCES_ID
        ws[f'B{row_idx}'] = district[1]  # District_Name
        ws[f'C{row_idx}'] = district[2]  # County
        ws[f'D{row_idx}'] = district[3]  # Locale_Code

        # E: Locale_Category formula
        ws[f'E{row_idx}'] = f'=IFS(D{row_idx}<=13,"City",D{row_idx}<=23,"Suburb",D{row_idx}<=33,"Town",TRUE,"Rural")'

        # F: Locale_Label formula
        ws[f'F{row_idx}'] = f'=IFS(D{row_idx}=11,"City-Large",D{row_idx}=12,"City-Midsize",D{row_idx}=13,"City-Small",D{row_idx}=21,"Suburb-Large",D{row_idx}=22,"Suburb-Midsize",D{row_idx}=23,"Suburb-Small",D{row_idx}=31,"Town-Fringe",D{row_idx}=32,"Town-Distant",D{row_idx}=33,"Town-Remote",D{row_idx}=41,"Rural-Fringe",D{row_idx}=42,"Rural-Distant",D{row_idx}=43,"Rural-Remote",TRUE,"ERROR-CHECK-CODE")'

        ws[f'G{row_idx}'] = district[4]  # Enrollment
        ws[f'H{row_idx}'] = district[5]  # FRL_Count
        ws[f'I{row_idx}'] = district[6]  # FRL_Percent

        # J: Has_CTE formula
        ws[f'J{row_idx}'] = f'=IF(COUNTIFS(tbl_Programs_Raw[NCES_ID],A{row_idx})>0,"Yes","No")'

        # K-N: Regional assignments via VLOOKUP
        ws[f'K{row_idx}'] = f'=IFERROR(VLOOKUP(C{row_idx},tbl_Geographic_Crosswalk,2,FALSE),"Unknown")'
        ws[f'L{row_idx}'] = f'=IFERROR(VLOOKUP(C{row_idx},tbl_Geographic_Crosswalk,3,FALSE),"Unknown")'
        ws[f'M{row_idx}'] = f'=IFERROR(VLOOKUP(C{row_idx},tbl_Geographic_Crosswalk,4,FALSE),"Unknown")'
        ws[f'N{row_idx}'] = f'=IFERROR(VLOOKUP(C{row_idx},tbl_Geographic_Crosswalk,5,FALSE),"Unknown")'

    # Create table
    table_ref = f"A1:N{len(DISTRICTS_DATA) + 1}"
    tab = Table(displayName="tbl_Districts_Clean", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Auto-adjust columns
    for col_idx in range(1, 15):
        ws.column_dimensions[get_column_letter(col_idx)].width = 20

    set_tab_color(ws, "ADD8E6")

    return ws


def create_programs_fractional_sheet(wb):
    """Sheet 12: Programs_Fractional"""
    ws = wb.create_sheet("Programs_Fractional")

    headers = ["NCES_ID", "CIP_Code", "Building_Code", "Program_Name", "Program_Status",
               "Is_InHouse", "Sharing_Count", "Fractional_Credit"]

    # Write headers
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    # Write data with formulas
    for row_idx, program in enumerate(PROGRAMS_DATA, 2):
        ws[f'A{row_idx}'] = program[0]  # NCES_ID
        ws[f'B{row_idx}'] = program[1]  # CIP_Code
        ws[f'C{row_idx}'] = program[2]  # Building_Code
        ws[f'D{row_idx}'] = program[3]  # Program_Name
        ws[f'E{row_idx}'] = program[4]  # Program_Status

        # F: Is_InHouse formula
        ws[f'F{row_idx}'] = f'=IF(LEFT(TEXT(C{row_idx},"00000000"),5)=LEFT(TEXT(A{row_idx},"00000000"),5),"Yes","No")'

        # G: Sharing_Count formula
        ws[f'G{row_idx}'] = f'=IF(F{row_idx}="Yes",1,COUNTIFS(tbl_Programs_Raw[Building_Code],C{row_idx}))'

        # H: Fractional_Credit formula
        ws[f'H{row_idx}'] = f'=IF(F{row_idx}="Yes",1,1/G{row_idx})'

    # Create table
    table_ref = f"A1:H{len(PROGRAMS_DATA) + 1}"
    tab = Table(displayName="tbl_Programs_Fractional", ref=table_ref)
    style = TableStyleInfo(name="TableStyleMedium2", showFirstColumn=False, showLastColumn=False, showRowStripes=True, showColumnStripes=False)
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Auto-adjust columns
    for col_idx in range(1, 9):
        ws.column_dimensions[get_column_letter(col_idx)].width = 20

    set_tab_color(ws, "ADD8E6")

    return ws


def create_toggle_settings_sheet(wb):
    """Sheet 13: Toggle_Settings"""
    ws = wb.create_sheet("Toggle_Settings")

    # Title
    ws['A1'] = "SENSITIVITY ANALYSIS TOGGLE PANEL"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:C1')

    # Labels and dropdowns
    ws['A2'] = "District Inclusion:"
    ws['B2'] = "All Districts"
    ws['C2'] = "Current: All Districts / CTE-Only"

    ws['A3'] = "Wage Threshold:"
    ws['B3'] = "120%"
    ws['C3'] = "Current: 110% / 120% / 130%"

    ws['A4'] = "Occupation Count:"
    ws['B4'] = "Top 15"
    ws['C4'] = "Current: Top 15 / Top 20"

    ws['A5'] = "Time Reference:"
    ws['B5'] = "Current"
    ws['C5'] = "Current: Current / 10-Year Projection"

    ws['A7'] = "CONFIGURATION NOTES:"
    ws['A7'].font = BOLD_FONT
    ws['A8'] = "Changes to settings automatically update all PAI calculations"
    ws['A9'] = "Record your configuration before exporting to R"
    ws['A10'] = "Primary Analysis: CTE-Only, 120%, Top 15, Current"

    # Data validation for B2
    dv1 = DataValidation(type="list", formula1='"All Districts,CTE-Only"', allow_blank=False)
    ws.add_data_validation(dv1)
    dv1.add(ws['B2'])

    # Data validation for B3
    dv2 = DataValidation(type="list", formula1='"110%,120%,130%"', allow_blank=False)
    ws.add_data_validation(dv2)
    dv2.add(ws['B3'])

    # Data validation for B4
    dv3 = DataValidation(type="list", formula1='"Top 15,Top 20"', allow_blank=False)
    ws.add_data_validation(dv3)
    dv3.add(ws['B4'])

    # Data validation for B5
    dv4 = DataValidation(type="list", formula1='"Current,10-Year Projection"', allow_blank=False)
    ws.add_data_validation(dv4)
    dv4.add(ws['B5'])

    # Formatting
    ws['B2'].fill = YELLOW_FILL
    ws['B3'].fill = YELLOW_FILL
    ws['B4'].fill = YELLOW_FILL
    ws['B5'].fill = YELLOW_FILL

    for cell_ref in ['A2', 'A3', 'A4', 'A5']:
        ws[cell_ref].font = BOLD_FONT

    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 50

    set_tab_color(ws, "FFFF99")

    return ws


def create_variable_codebook_sheet(wb):
    """Sheet 23: Variable_Codebook"""
    ws = wb.create_sheet("Variable_Codebook")

    headers = ["Variable_Name", "Data_Type", "Valid_Range", "Description", "Source_Sheet", "Formula_Reference"]

    data = [
        ["NCES_ID", "Text", "7-digit", "National Center for Education Statistics ID", "Districts_Raw", "N/A"],
        ["District_Name", "Text", "-", "Official district name", "Districts_Raw", "N/A"],
        ["County", "Text", "-", "Michigan county name", "Districts_Raw", "N/A"],
        ["Locale_Code", "Integer", "11-43", "NCES Urban-Centric Locale Code", "Districts_Raw", "N/A"],
        ["Locale_Category", "Text", "City/Suburb/Town/Rural", "Broad geographic classification", "Districts_Clean", "IFS(Locale_Code...)"],
        ["Locale_Label", "Text", "12 categories", "Detailed locale classification", "Districts_Clean", "IFS(Locale_Code...)"],
        ["Enrollment", "Integer", ">0", "Total district enrollment", "Districts_Raw", "N/A"],
        ["FRL_Count", "Integer", ">=0", "Students eligible for Free/Reduced Lunch", "Districts_Raw", "N/A"],
        ["FRL_Percent", "Decimal", "0-100", "Free/Reduced Lunch percentage", "Districts_Raw", "Calculated"],
        ["Has_CTE", "Text", "Yes/No", "District offers CTE programs", "Districts_Clean", "COUNTIFS"],
        ["CIP_Code", "Text", "6-digit", "Classification of Instructional Programs code", "Programs_Raw", "N/A"],
        ["Building_Code", "Text", "8-digit", "Facility/program location identifier", "Programs_Raw", "N/A"],
        ["Program_Name", "Text", "-", "CTE program title", "Programs_Raw", "N/A"],
        ["Program_Status", "Text", "Active/Inactive", "Current program operational status", "Programs_Raw", "N/A"],
        ["Is_InHouse", "Text", "Yes/No", "Program delivered within district", "Programs_Fractional", "IF(LEFT...)"],
        ["Sharing_Count", "Integer", ">=1", "Number of districts sharing program facility", "Programs_Fractional", "COUNTIFS"],
        ["Fractional_Credit", "Decimal", "0-1", "Program access credit for shared programs", "Programs_Fractional", "IF(Is_InHouse...)"],
        ["SOC_Code", "Text", "7-digit", "Standard Occupational Classification code", "Labor_Market", "N/A"],
        ["Occupation_Title", "Text", "-", "Job title from SOC taxonomy", "Labor_Market", "N/A"],
        ["Median_Wage", "Integer", ">0", "Occupation median annual wage", "Labor_Market", "N/A"],
        ["Regional_Median_Wage", "Integer", ">0", "Overall regional median wage benchmark", "Labor_Market", "N/A"],
        ["Annual_Openings_Current", "Integer", ">=0", "Current year projected job openings", "Labor_Market", "N/A"],
        ["Annual_Openings_10yr", "Integer", ">=0", "10-year projection job openings", "Labor_Market", "N/A"],
        ["CEPD_Region", "Text", "-", "Career Education Planning District", "Geographic_Crosswalk", "N/A"],
        ["Prosperity_Region", "Text", "-", "Michigan Prosperity Region", "Geographic_Crosswalk", "N/A"],
        ["Metropolitan_Region", "Text", "-", "Metropolitan Statistical Area", "Geographic_Crosswalk", "N/A"],
        ["Economic_Region", "Text", "-", "Economic development region", "Geographic_Crosswalk", "N/A"],
        ["Perkins_Funding", "Integer", ">0", "Carl D. Perkins federal funding amount", "Control_Variables_Raw", "N/A"],
        ["Unemployment_Rate", "Decimal", "0-20", "County unemployment rate percentage", "Control_Variables_Raw", "N/A"],
        ["District_Wealth_Index", "Decimal", "0-3", "Relative district wealth indicator", "Control_Variables_Raw", "N/A"],
        ["Urbanicity_Score", "Integer", "0-100", "Composite urban/rural density score", "Control_Variables_Raw", "N/A"],
    ]

    table_ref = f"A1:F{len(data) + 1}"
    create_table(ws, "tbl_Variable_Codebook", table_ref, data, headers)

    # Adjust column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 50
    ws.column_dimensions['E'].width = 20
    ws.column_dimensions['F'].width = 30

    set_tab_color(ws, "E6E6FA")

    return ws


def create_formula_key_sheet(wb):
    """Sheet 24: Formula_Key"""
    ws = wb.create_sheet("Formula_Key")

    headers = ["Formula_Name", "Sheet_Location", "Formula_Text", "Plain_Language_Explanation", "Example"]

    data = [
        ["Locale_Category", "Districts_Clean, Column E", '=IFS([@Locale_Code]<=13,"City",[@Locale_Code]<=23,"Suburb",[@Locale_Code]<=33,"Town",TRUE,"Rural")', "If locale code 11-13 then City; 21-23 then Suburb; 31-33 then Town; 41-43 then Rural", "Locale_Code=11 → City"],
        ["Locale_Label", "Districts_Clean, Column F", '=IFS([@Locale_Code]=11,"City-Large",[...12 conditions...])', "Maps each 2-digit locale code to detailed 12-category classification", "Locale_Code=21 → Suburb-Large"],
        ["Has_CTE", "Districts_Clean, Column J", "=IF(COUNTIFS(tbl_Programs_Raw[NCES_ID],[@NCES_ID])>0,\"Yes\",\"No\")", "Checks if district has any programs in Programs_Raw table; Yes if count > 0", "NCES_ID has 3 programs → Yes"],
        ["CEPD_Region", "Districts_Clean, Column K", "=IFERROR(VLOOKUP([@County],tbl_Geographic_Crosswalk,2,FALSE),\"Unknown\")", "Looks up county in Geographic_Crosswalk and returns CEPD_Region (column 2)", "Wayne County → Southeast"],
        ["Is_InHouse", "Programs_Fractional, Column F", '=IF(LEFT(TEXT([@Building_Code],"00000000"),5)=LEFT(TEXT([@NCES_ID],"00000000"),5),"Yes","No")', "Compares first 5 digits of Building_Code to first 5 of NCES_ID; match means in-house", "Building 26000100, NCES 2600010 → Yes"],
        ["Sharing_Count", "Programs_Fractional, Column G", "=IF([@Is_InHouse]=\"Yes\",1,COUNTIFS(tbl_Programs_Raw[Building_Code],[@Building_Code]))", "If in-house return 1; otherwise count how many districts share this Building_Code", "Building 81050100 shared by 3 districts → 3"],
        ["Fractional_Credit", "Programs_Fractional, Column H", "=IF([@Is_InHouse]=\"Yes\",1,1/[@Sharing_Count])", "If program in-house get full credit (1.0); if shared divide 1 by number of sharing districts", "3 districts share program → each gets 0.333"],
        ["StatePathways_Count", "Parameters, Named Range", "=Parameters!$B$2", "Total number of CTE pathways available statewide (user-defined parameter)", "Default value = 50"],
        ["State_Total_Programs", "Named Range", "=SUM(tbl_Programs_Fractional[Fractional_Credit])", "Sum all fractional credits across all districts; represents total program availability", "Used in PDER calculations"],
        ["State_Total_Enrollment", "Named Range", "=SUM(tbl_Districts_Clean[Enrollment])", "Sum enrollment across all districts in cleaned data", "Used in PDER calculations"],
    ]

    table_ref = f"A1:E{len(data) + 1}"
    create_table(ws, "tbl_Formula_Key", table_ref, data, headers)

    # Adjust column widths
    ws.column_dimensions['A'].width = 20
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 60
    ws.column_dimensions['D'].width = 70
    ws.column_dimensions['E'].width = 35

    set_tab_color(ws, "E6E6FA")

    return ws


def create_named_ranges(wb):
    """Create named ranges in workbook"""

    # Define named ranges
    named_ranges = {
        "StatePathways_Count": "Parameters!$B$2",
        "Active_Toggle_District": "Toggle_Settings!$B$2",
        "Active_Toggle_Wage": "Toggle_Settings!$B$3",
        "Active_Toggle_OccCount": "Toggle_Settings!$B$4",
        "Active_Toggle_TimeRef": "Toggle_Settings!$B$5",
    }

    for name, reference in named_ranges.items():
        defn = DefinedName(name=name, attr_text=reference)
        wb.defined_names.add(defn)

    print(f"✓ Created {len(named_ranges)} named ranges")


def main():
    """Main execution function"""
    print("=" * 60)
    print("CTE RESEARCH MASTER WORKBOOK - PHASE 1 BUILDER")
    print("=" * 60)

    # Create workbook
    wb = Workbook()

    # Remove default sheet
    default_sheet = wb.active
    wb.remove(default_sheet)

    print("\n📋 Creating sheets...")

    # Section A: Raw Data Sheets (00-10)
    print("  → Sheet 00: Parameters")
    create_parameters_sheet(wb)

    print("  → Sheet 01: Districts_Raw")
    create_districts_raw_sheet(wb)

    print("  → Sheet 02: Programs_Raw")
    create_programs_raw_sheet(wb)

    print("  → Sheets 03-07: Labor_Market (5 geographic levels)")
    create_labor_market_sheets(wb)

    print("  → Sheet 08: CIP_SOC_Crosswalk")
    create_cip_soc_crosswalk_sheet(wb)

    print("  → Sheet 09: Geographic_Crosswalk")
    create_geographic_crosswalk_sheet(wb)

    print("  → Sheet 10: Control_Variables_Raw")
    create_control_variables_sheet(wb)

    # Section B: Processed Data Sheets (11-13)
    print("  → Sheet 11: Districts_Clean")
    create_districts_clean_sheet(wb)

    print("  → Sheet 12: Programs_Fractional")
    create_programs_fractional_sheet(wb)

    print("  → Sheet 13: Toggle_Settings")
    create_toggle_settings_sheet(wb)

    # Section C: Documentation Sheets (23-24)
    print("  → Sheet 23: Variable_Codebook")
    create_variable_codebook_sheet(wb)

    print("  → Sheet 24: Formula_Key")
    create_formula_key_sheet(wb)

    # Create named ranges
    print("\n📌 Creating named ranges...")
    create_named_ranges(wb)

    # Save workbook
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"CTE_Research_Master_Phase1_{timestamp}.xlsx"
    wb.save(filename)

    print(f"\n✅ Workbook created successfully: {filename}")
    print(f"   Total sheets: {len(wb.sheetnames)}")
    print(f"   Named ranges: {len(wb.defined_names)}")
    print("\n" + "=" * 60)

    return filename


if __name__ == "__main__":
    main()
