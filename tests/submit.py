from higgs_dna.submission.lxplus import LXPlusVanillaSubmitter


analysis_name = "GluGluH_125_postEE"
analysis_dict = {
    "samplejson": "sample_json/ggh_125_post.json",
    "workflow": "dystudies",
    "metaconditions": "Era2017_legacy_v1",
    "year": {
        "GluGluHtoGG_M-125_postEE": [
            "2022postEE"
        ]
    },
    "taggers": [],
    "systematics": {
        "GluGluHtoGG_M-125_postEE": [
            "Pileup",
            "Scale",
            "Smearing",
            "energyErrShift",
            "AlphaS",
            "PartonShower",
            "LHEScale",
            "LHEPdf",
            "ElectronVetoSF",
            "PreselSF",
            "TriggerSF",
            "Material",
            "FNUF"
        ]
    },
    "corrections": {
        "GluGluHtoGG_M-125_postEE": [
            "Pileup",
            "Smearing",
            "energyErrShift",
            "ElectronVetoSF",
            "PreselSF",
            "TriggerSF",
            "jerc_jet_syst",
            "Material",
            "FNUF"
        ]
    }
}
original_analysis_path = "/eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/ggh_125_post_analysis.json"
sample_dict = {
    "GluGluHtoGG_M-125_postEE": [
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_2.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_14.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_7.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_1.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_17.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_10.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_11.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_12.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_9.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_18.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_4.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_16.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_8.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_13.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_5.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_6.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_15.root",
        "root://xrootd-cms.infn.it//store/user/chpan/GluGlutoH_125_postEE/GluGluHtoGG_M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/crab_Private_HggNANO_Run3_2022_GluGluH_125_post/241203_131726/0000/HIG-Run3Summer22EENanoAODv13-00004_3.root"
    ]
}
args_string = "--dump /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/output_score/ --json-analysis /eos/user/c/chpan/higgs_dna_1205/HiggsDNA/tests/config_files/ggh_125_post_analysis.json --doDeco --doFlow_corrections --Smear_sigma_m --fiducialCuts geometric"

submitter = LXPlusVanillaSubmitter(analysis_name,
        analysis_dict,
        original_analysis_path,
        sample_dict,
        args_string,
)

submitter.submit()
