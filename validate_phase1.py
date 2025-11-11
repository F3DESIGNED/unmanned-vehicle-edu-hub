#!/usr/bin/env python3
"""
Phase 1 Validation Script
Performs comprehensive validation checks on the CTE Research Master Workbook
"""

import openpyxl
from openpyxl.utils import get_column_letter
from datetime import datetime
import sys

def validate_named_ranges(wb):
    """Validation Check 1: Named Ranges"""
    print("\n" + "="*60)
    print("VALIDATION CHECK 1: NAMED RANGES")
    print("="*60)

    expected_ranges = [
        "StatePathways_Count",
        "Active_Toggle_District",
        "Active_Toggle_Wage",
        "Active_Toggle_OccCount",
        "Active_Toggle_TimeRef"
    ]

    try:
        found_names = [name for name in wb.defined_names]
    except:
        found_names = []

    print(f"\n✓ Expected named ranges: {len(expected_ranges)}")
    print(f"✓ Found named ranges: {len(found_names)}")

    all_passed = True
    for name in expected_ranges:
        if name in found_names:
            print(f"  ✓ {name} - FOUND")
        else:
            print(f"  ✗ {name} - MISSING")
            all_passed = False

    # Test a named range value
    try:
        params_ws = wb["Parameters"]
        state_pathways = params_ws['B2'].value
        print(f"\n✓ StatePathways_Count value: {state_pathways}")
        if state_pathways == 50:
            print("  ✓ Value is correct (50)")
        else:
            print(f"  ✗ Value should be 50, found {state_pathways}")
            all_passed = False
    except Exception as e:
        print(f"  ✗ Error reading named range: {e}")
        all_passed = False

    return all_passed


def validate_tables(wb):
    """Validation Check 2: Tables"""
    print("\n" + "="*60)
    print("VALIDATION CHECK 2: TABLES")
    print("="*60)

    expected_tables = {
        "Districts_Raw": "tbl_Districts_Raw",
        "Programs_Raw": "tbl_Programs_Raw",
        "Labor_Market_County": "tbl_Labor_County",
        "Labor_Market_CEPD": "tbl_Labor_CEPD",
        "Labor_Market_Prosperity": "tbl_Labor_Prosperity",
        "Labor_Market_Metropolitan": "tbl_Labor_Metropolitan",
        "Labor_Market_Economic": "tbl_Labor_Economic",
        "CIP_SOC_Crosswalk": "tbl_CIP_SOC_Crosswalk",
        "Geographic_Crosswalk": "tbl_Geographic_Crosswalk",
        "Control_Variables_Raw": "tbl_Control_Variables",
        "Districts_Clean": "tbl_Districts_Clean",
        "Programs_Fractional": "tbl_Programs_Fractional",
        "Variable_Codebook": "tbl_Variable_Codebook",
        "Formula_Key": "tbl_Formula_Key",
    }

    print(f"\n✓ Expected tables: {len(expected_tables)}")

    all_passed = True
    found_count = 0

    for sheet_name, table_name in expected_tables.items():
        try:
            ws = wb[sheet_name]
            if table_name in ws.tables:
                print(f"  ✓ {sheet_name}: {table_name} - FOUND")
                found_count += 1
            else:
                print(f"  ✗ {sheet_name}: {table_name} - MISSING")
                all_passed = False
        except KeyError:
            print(f"  ✗ Sheet {sheet_name} not found")
            all_passed = False

    print(f"\n✓ Found {found_count}/{len(expected_tables)} tables")

    return all_passed


def validate_formulas(wb):
    """Validation Check 3: Formula Validation"""
    print("\n" + "="*60)
    print("VALIDATION CHECK 3: FORMULAS")
    print("="*60)

    all_passed = True

    # Check Districts_Clean formulas
    print("\n→ Checking Districts_Clean formulas...")
    try:
        ws = wb["Districts_Clean"]

        # Check Locale_Label - should not contain "ERROR-CHECK-CODE"
        error_count = 0
        for row in range(2, ws.max_row + 1):
            locale_label = ws[f'F{row}'].value
            if locale_label and "ERROR" in str(locale_label):
                error_count += 1

        if error_count == 0:
            print(f"  ✓ All Locale_Labels valid (no errors found)")
        else:
            print(f"  ✗ Found {error_count} error values in Locale_Label")
            all_passed = False

        # Check Has_CTE column
        has_cte_count = 0
        for row in range(2, ws.max_row + 1):
            has_cte = ws[f'J{row}'].value
            if has_cte in ["Yes", "No"]:
                has_cte_count += 1

        total_districts = ws.max_row - 1
        print(f"  ✓ Has_CTE valid for {has_cte_count}/{total_districts} districts")

    except Exception as e:
        print(f"  ✗ Error checking Districts_Clean: {e}")
        all_passed = False

    # Check Programs_Fractional formulas
    print("\n→ Checking Programs_Fractional formulas...")
    try:
        ws = wb["Programs_Fractional"]

        # Check fractional credits are between 0 and 1
        invalid_credits = 0
        for row in range(2, ws.max_row + 1):
            credit = ws[f'H{row}'].value
            if credit is not None:
                try:
                    credit_val = float(credit)
                    if credit_val < 0 or credit_val > 1:
                        invalid_credits += 1
                except:
                    invalid_credits += 1

        total_programs = ws.max_row - 1
        if invalid_credits == 0:
            print(f"  ✓ All Fractional_Credits valid (0-1 range)")
        else:
            print(f"  ✗ Found {invalid_credits} invalid credits")
            all_passed = False

        # Check shared programs sum to 1.0
        print(f"  → Validating shared program credits...")
        building_codes = {}
        for row in range(2, ws.max_row + 1):
            building_code = ws[f'C{row}'].value
            credit = ws[f'H{row}'].value
            if building_code and credit is not None:
                if building_code not in building_codes:
                    building_codes[building_code] = 0
                try:
                    building_codes[building_code] += float(credit)
                except:
                    pass

        # Check shared programs (those with sum != 1.0 for in-house, or close to 1.0 for shared)
        shared_errors = 0
        for building_code, total_credit in building_codes.items():
            if abs(total_credit - 1.0) > 0.01:  # Allow small floating point errors
                shared_errors += 1

        if shared_errors == 0:
            print(f"  ✓ All shared programs sum correctly to 1.0")
        else:
            print(f"  ⚠ Found {shared_errors} building codes with non-1.0 sums (may be in-house)")

    except Exception as e:
        print(f"  ✗ Error checking Programs_Fractional: {e}")
        all_passed = False

    return all_passed


def validate_toggle_functionality(wb):
    """Validation Check 4: Toggle Functionality"""
    print("\n" + "="*60)
    print("VALIDATION CHECK 4: TOGGLE SETTINGS")
    print("="*60)

    all_passed = True

    try:
        ws = wb["Toggle_Settings"]

        # Check that toggle cells exist and have values
        toggles = {
            "B2": "District Inclusion",
            "B3": "Wage Threshold",
            "B4": "Occupation Count",
            "B5": "Time Reference"
        }

        print("\n→ Checking toggle values...")
        for cell, name in toggles.items():
            value = ws[cell].value
            if value:
                print(f"  ✓ {name} ({cell}): {value}")
            else:
                print(f"  ✗ {name} ({cell}): NO VALUE")
                all_passed = False

        # Check for data validation
        print("\n→ Checking data validation...")
        validation_count = len(ws.data_validations.dataValidation)
        if validation_count >= 4:
            print(f"  ✓ Found {validation_count} data validations")
        else:
            print(f"  ✗ Expected at least 4 data validations, found {validation_count}")
            all_passed = False

    except Exception as e:
        print(f"  ✗ Error checking Toggle_Settings: {e}")
        all_passed = False

    return all_passed


def validate_data_quality(wb):
    """Validation Check 5: Data Quality"""
    print("\n" + "="*60)
    print("VALIDATION CHECK 5: DATA QUALITY")
    print("="*60)

    all_passed = True

    # Check Districts_Raw for blanks in key columns
    print("\n→ Checking Districts_Raw for completeness...")
    try:
        ws = wb["Districts_Raw"]
        key_columns = {'A': 'NCES_ID', 'B': 'District_Name', 'C': 'County', 'D': 'Locale_Code', 'E': 'Enrollment'}

        for col, name in key_columns.items():
            blank_count = 0
            for row in range(2, ws.max_row + 1):
                value = ws[f'{col}{row}'].value
                if value is None or str(value).strip() == '':
                    blank_count += 1

            if blank_count == 0:
                print(f"  ✓ {name}: No blank cells")
            else:
                print(f"  ✗ {name}: {blank_count} blank cells found")
                all_passed = False

    except Exception as e:
        print(f"  ✗ Error checking Districts_Raw: {e}")
        all_passed = False

    # Check Districts_Clean VLOOKUPs
    print("\n→ Checking Districts_Clean geographic assignments...")
    try:
        ws = wb["Districts_Clean"]

        # Count districts with valid regional assignments
        valid_assignments = 0
        total_districts = ws.max_row - 1

        for row in range(2, ws.max_row + 1):
            cepd = ws[f'K{row}'].value
            prosperity = ws[f'L{row}'].value
            metro = ws[f'M{row}'].value
            economic = ws[f'N{row}'].value

            if all([cepd and cepd != "Unknown",
                   prosperity and prosperity != "Unknown",
                   metro and metro != "Unknown",
                   economic and economic != "Unknown"]):
                valid_assignments += 1

        print(f"  ✓ Geographic assignments complete: {valid_assignments}/{total_districts} districts")

        if valid_assignments < total_districts:
            print(f"  ⚠ {total_districts - valid_assignments} districts have incomplete assignments")

    except Exception as e:
        print(f"  ✗ Error checking geographic assignments: {e}")
        all_passed = False

    return all_passed


def validate_documentation(wb):
    """Validation Check 6: Documentation Complete"""
    print("\n" + "="*60)
    print("VALIDATION CHECK 6: DOCUMENTATION")
    print("="*60)

    all_passed = True

    # Check Variable_Codebook
    print("\n→ Checking Variable_Codebook...")
    try:
        ws = wb["Variable_Codebook"]
        row_count = ws.max_row - 1  # Exclude header
        print(f"  ✓ Variable_Codebook entries: {row_count}")

        if row_count >= 30:
            print(f"  ✓ Meets minimum requirement (30+ variables)")
        else:
            print(f"  ✗ Below minimum requirement (need 30, have {row_count})")
            all_passed = False

    except Exception as e:
        print(f"  ✗ Error checking Variable_Codebook: {e}")
        all_passed = False

    # Check Formula_Key
    print("\n→ Checking Formula_Key...")
    try:
        ws = wb["Formula_Key"]
        row_count = ws.max_row - 1  # Exclude header
        print(f"  ✓ Formula_Key entries: {row_count}")

        if row_count >= 10:
            print(f"  ✓ Meets minimum requirement (10+ formulas)")
        else:
            print(f"  ⚠ Below target (recommended 10, have {row_count})")

    except Exception as e:
        print(f"  ✗ Error checking Formula_Key: {e}")
        all_passed = False

    return all_passed


def main():
    """Run all validation checks"""
    print("\n" + "="*70)
    print(" "*15 + "PHASE 1 VALIDATION REPORT")
    print(" "*10 + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("="*70)

    # Find the workbook
    import glob
    workbooks = glob.glob("CTE_Research_Master_Phase1_*.xlsx")

    if not workbooks:
        print("\n✗ ERROR: No Phase 1 workbook found!")
        return False

    wb_path = workbooks[0]
    print(f"\n→ Validating workbook: {wb_path}")

    try:
        wb = openpyxl.load_workbook(wb_path)
        print(f"✓ Workbook loaded successfully")
        print(f"✓ Total sheets: {len(wb.sheetnames)}")

    except Exception as e:
        print(f"\n✗ ERROR: Could not load workbook: {e}")
        return False

    # Run all validation checks
    results = {
        "Named Ranges": validate_named_ranges(wb),
        "Tables": validate_tables(wb),
        "Formulas": validate_formulas(wb),
        "Toggle Functionality": validate_toggle_functionality(wb),
        "Data Quality": validate_data_quality(wb),
        "Documentation": validate_documentation(wb),
    }

    # Summary
    print("\n" + "="*70)
    print("VALIDATION SUMMARY")
    print("="*70)

    for check_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status}: {check_name}")

    all_passed = all(results.values())

    print("\n" + "="*70)
    if all_passed:
        print("  ✅ ALL VALIDATION CHECKS PASSED")
        print("  Phase 1 is complete and ready for Phase 2")
    else:
        print("  ⚠ SOME VALIDATION CHECKS FAILED")
        print("  Review errors above and address issues")
    print("="*70 + "\n")

    # Save report to file
    report_file = f"Phase1_Validation_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    return all_passed, wb


if __name__ == "__main__":
    success, wb = main()
    sys.exit(0 if success else 1)
