#!/bin/bash

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/ggh_125_post_analysis.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/GJet_inclusive_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/data_E.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/data_F.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/data_G.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/pp-gg_80_post_analysis.json --executor vanilla_lxplus --queue longlunch

# QCD
python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-200to400_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-400to600_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-600to800_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-800to1000_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-1000to1200_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-1200to1500_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-1500to2000_postEE.json --executor vanilla_lxplus --queue longlunch

python /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/run_analysis.py --dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_FatJet_singlePhoton/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/QCD-4Jets_HT-2000_postEE.json --executor vanilla_lxplus --queue longlunch