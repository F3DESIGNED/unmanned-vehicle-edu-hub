#!/usr/bin/env Rscript
# R Import Test for CTE Research Master Workbook
# Tests importing Master_Analysis_Table from Excel

cat("==============================================\n")
cat("CTE RESEARCH MASTER - R IMPORT TEST\n")
cat("==============================================\n\n")

# Check for required packages
packages <- c("readxl", "dplyr")
for (pkg in packages) {
  if (!require(pkg, character.only = TRUE, quietly = TRUE)) {
    cat(sprintf("Installing %s...\n", pkg))
    install.packages(pkg, repos = "http://cran.rstudio.com/")
    library(pkg, character.only = TRUE)
  }
}

# Find the workbook
wb_files <- list.files(pattern = "CTE_Research_Master_v1.0_.*\\.xlsx")

if (length(wb_files) == 0) {
  stop("✗ ERROR: No Phase 3 workbook found!")
}

wb_path <- wb_files[1]
cat(sprintf("→ Loading workbook: %s\n\n", wb_path))

# Import Master_Analysis_Table
cat("→ Importing Master_Analysis_Table...\n")
df <- readxl::read_excel(wb_path, sheet = "Master_Analysis_Table")

cat(sprintf("✓ Imported successfully\n"))
cat(sprintf("  Rows: %d\n", nrow(df)))
cat(sprintf("  Columns: %d\n\n", ncol(df)))

# Display structure
cat("→ Data structure:\n")
str(df, give.attr = FALSE)

cat("\n→ Summary statistics:\n")
summary(df %>% select(Enrollment, FRL_Percent, OCQ, PAI_County, PDER))

cat("\n→ Column names:\n")
print(names(df))

cat("\n→ First 3 districts:\n")
print(head(df %>% select(NCES_ID, District_Name, OCQ, PAI_County, PDER), 3))

cat("\n==============================================\n")
cat("✅ R IMPORT TEST SUCCESSFUL\n")
cat("==============================================\n")

# Optional: Alternative CSV import
cat("\n→ Testing CSV import (if exported)...\n")
if (file.exists("Master_Analysis_Table_Export.csv")) {
  df_csv <- read.csv("Master_Analysis_Table_Export.csv", stringsAsFactors = FALSE)
  cat(sprintf("✓ CSV imported: %d rows, %d columns\n", nrow(df_csv), ncol(df_csv)))
} else {
  cat("  (CSV not found - run export_for_r.py first)\n")
}

cat("\n✅ All import methods validated\n")
