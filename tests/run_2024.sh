#!/bin/bash

# signal
python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/ggh_125_2024_analysis.json --no-trigger --executor vanilla_lxplus --queue longlunch

# background MC

## QCD samples
python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-200to400_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-400to600_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-600to800_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-800to1000_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-1000to1200_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-1200to1500_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-1500to2000_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-2000_2024.json --no-trigger --executor vanilla_lxplus --queue longlunch

## GJet samples
python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/GJet_Bin-MGG-80-PT40.json --no-trigger --executor vanilla_lxplus --queue longlunch

# data samples
python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_2024/no_presel/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/2024_Egamma0_dataC.json --no-trigger --executor vanilla_lxplus --queue longlunch