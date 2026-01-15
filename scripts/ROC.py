import glob
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve, auc

# =========================
# 文件路径
# =========================
signal_files = glob.glob("signal/*.parquet")
background_files = glob.glob("background/*.parquet")

# =========================
# 变量名
# =========================
score_name = "Hgg_score_gloparT3"
weight_name = "weight"
mass_name = "softdropmass_raw"
presel_name = "pass_presel_fiducialcut"

# =========================
# 只读取这些 branch（非常重要）
# =========================
signal_columns = [
    score_name,
    weight_name,
    "deltaR_leadGenPho",
    "deltaR_subleadGenPho",
    presel_name
]
background_columns = [score_name, mass_name, presel_name]


def extra_cuts(arr, is_signal=False, add_precut=False):
    """
    通用 cut 接口
    """
    if add_precut:
        mask = (arr[presel_name] == True)
    else:
        mask = ak.ones_like(arr[score_name], dtype=bool)
    if is_signal:
        return (
            (arr.deltaR_leadGenPho < 0.8) &
            (arr.deltaR_subleadGenPho < 0.8) & (arr[score_name] > -1) & mask
        )
    else:
        return (arr[score_name] > -1) & mask

def load_signal(files, add_precut=False):
    scores = []
    weights = []

    for f in files:
        arr = ak.from_parquet(
            f,
            columns=signal_columns
        )

        mask = extra_cuts(arr, is_signal=True, add_precut=add_precut)

        scores.append(arr[score_name][mask])
        weights.append(arr[weight_name][mask])

    return (
        ak.to_numpy(ak.concatenate(scores)),
        ak.to_numpy(ak.concatenate(weights)),
    )


def load_background(files, add_precut=False):
    scores = []

    for f in files:
        arr = ak.from_parquet(
            f,
            columns=background_columns
        )

        mass_mask = (
            ((arr[mass_name] > 100) & (arr[mass_name] < 120)) |
            ((arr[mass_name] > 130) & (arr[mass_name] < 180))
        )

        mask = mass_mask & extra_cuts(arr, add_precut=add_precut)
        scores.append(arr[score_name][mask])

    return ak.to_numpy(ak.concatenate(scores))


if __name__ == "__main__":

    signal_scale = 20.64 * 2.27e-3 * 38.09e3

    # 读取数据
    sig_scores, sig_weights = load_signal(signal_files)
    bkg_scores = load_background(background_files)

    print(f"Signal events (weighted sum): {sig_weights.sum():.5f}")
    print(f"Background events: {len(bkg_scores)}")

    # 构造 sklearn 输入
    y_true = np.concatenate([
        np.ones(len(sig_scores)),
        np.zeros(len(bkg_scores))
    ])

    y_score = np.concatenate([
        sig_scores,
        bkg_scores
    ])

    sample_weight = np.concatenate([
        sig_weights,
        np.ones(len(bkg_scores))   # data：权重 = 1
    ])

    # 计算 ROC
    fpr, tpr, thresholds = roc_curve(
        y_true,
        y_score,
        sample_weight=sample_weight
    )

    roc_auc = auc(fpr, tpr)


    # 读取数据
    sig_scores_pre, sig_weights_pre = load_signal(signal_files, add_precut=True)
    bkg_scores_pre = load_background(background_files, add_precut=True)

    print(f"Signal events (weighted sum): {sig_weights_pre.sum():.5f}")
    print(f"Background events: {len(bkg_scores_pre)}")

    # 构造 sklearn 输入
    y_true_pre = np.concatenate([
        np.ones(len(sig_scores_pre)),
        np.zeros(len(bkg_scores_pre))
    ])

    y_score_pre = np.concatenate([
        sig_scores_pre,
        bkg_scores_pre
    ])

    sample_weight_pre = np.concatenate([
        sig_weights_pre,
        np.ones(len(bkg_scores_pre))   # data：权重 = 1
    ])

    # 计算 ROC
    fpr_pre, tpr_pre, thresholds_pre = roc_curve(
        y_true_pre,
        y_score_pre,
        sample_weight=sample_weight_pre
    )

    roc_auc_pre = auc(fpr_pre, tpr_pre)


    # 画图
    plt.figure(figsize=(6, 6))
    # plt.plot(tpr * sig_weights.sum() * signal_scale, fpr * len(bkg_scores), lw=2, label=f"No presel AUC = {roc_auc:.3f}")
    # plt.plot(tpr_pre * sig_weights_pre.sum() * signal_scale, fpr_pre * len(bkg_scores_pre), lw=2, label=f"With presel (AUC={roc_auc_pre:.3f})")
    plt.plot(tpr, fpr, lw=2, label=f"No presel AUC = {roc_auc:.3f}")
    plt.plot(tpr_pre, fpr_pre, lw=2, label=f"With presel (AUC={roc_auc_pre:.3f})")
    plt.xlabel("Signal efficiency")
    plt.ylabel("Background efficiency")
    plt.yscale("log")
    plt.text(0.95, 0.15, r"$H\rightarrow \gamma \gamma$ vs datasideband",
            transform=plt.gca().transAxes,  # 坐标相对轴范围（0~1）
            fontweight='bold',
            fontsize=15,
            color='black',
            ha='right', va='top')
    plt.text(0.95, 0.10, r"$100~\mathrm{GeV} < m_{\mathrm{SD}-raw} < 180~\mathrm{GeV}$",
            transform=plt.gca().transAxes,  # 坐标相对轴范围（0~1）
            fontsize=12,
            color='black',
            ha='right', va='top')
    plt.grid(True)
    plt.legend()
    plt.title("ROC curve (Hgg_score_gloparT3)")
    plt.tight_layout()
    plt.savefig("roc.png")
