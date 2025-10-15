# Anomaly Detection — Final Report

- **Run folder**: `/content/drive/MyDrive/anomaly_task2_outputs/run_20251015_181115`
- **Series total (train dir)**: 82
- **Series with metrics JSON**: 80
- **Series with positives in test**: 66
- **Series with NO positives in test**: 14

## Medians (ignoring NaN)
- Precision (median): **0.099**
- Recall (median): **0.994**
- F1 (median): **0.149**
- ROC AUC (median): **0.495**
- AUPRC (median): **0.062**

## Top-10 by F1
- **A-9 — F1=0.834, P=0.813, R=0.857, AUC=0.915, AUPRC=0.896**
- **D-7 — F1=0.698, P=0.539, R=0.993, AUC=0.755, AUPRC=0.549**
- **D-2 — F1=0.668, P=0.501, R=1.000, AUC=0.711, AUPRC=0.645**
- **D-3 — F1=0.662, P=0.495, R=0.999, AUC=0.407, AUPRC=0.316**
- **D-4 — F1=0.661, P=0.494, R=1.000, AUC=0.413, AUPRC=0.338**
- **A-8 — F1=0.658, P=0.491, R=0.998, AUC=0.448, AUPRC=0.424**
- **A-7 — F1=0.581, P=0.410, R=0.998, AUC=0.611, AUPRC=0.307**
- **F-2 — F1=0.572, P=0.401, R=1.000, AUC=0.585, AUPRC=0.370**
- **E-3 — F1=0.568, P=0.397, R=1.000, AUC=0.357, AUPRC=0.304**
- **D-1 — F1=0.564, P=0.393, R=1.000, AUC=0.165, AUPRC=0.275**

## Bottom-10 by F1 (with finite F1)
- **G-2 — F1=0.027, P=0.014, R=1.000, AUC=0.493, AUPRC=0.014**
- **G-3 — F1=0.028, P=0.014, R=1.000, AUC=0.488, AUPRC=0.014**
- **D-8 — F1=0.028, P=0.014, R=1.000, AUC=0.494, AUPRC=0.014**
- **A-1 — F1=0.033, P=0.017, R=1.000, AUC=0.495, AUPRC=0.017**
- **T-3 — F1=0.037, P=0.019, R=1.000, AUC=0.386, AUPRC=0.014**
- **M-2 — F1=0.038, P=0.019, R=1.000, AUC=0.032, AUPRC=0.010**
- **R-1 — F1=0.038, P=0.019, R=1.000, AUC=0.493, AUPRC=0.019**
- **F-1 — F1=0.040, P=0.021, R=0.438, AUC=0.402, AUPRC=0.015**
- **F-3 — F1=0.041, P=0.021, R=1.000, AUC=0.449, AUPRC=0.011**
- **D-6 — F1=0.046, P=0.025, R=0.357, AUC=0.435, AUPRC=0.016**

## Figures
- F1 histogram: `/content/drive/MyDrive/anomaly_task2_outputs/run_20251015_181115/hist_F1.png`
- Precision/Recall histogram: `/content/drive/MyDrive/anomaly_task2_outputs/run_20251015_181115/hist_Precision_Recall.png`

## Tables
- TOP10 CSV: `/content/drive/MyDrive/anomaly_task2_outputs/run_20251015_181115/TOP10_by_F1.csv`
- BOTTOM10 CSV: `/content/drive/MyDrive/anomaly_task2_outputs/run_20251015_181115/BOTTOM10_by_F1.csv`
- Unified events CSV: `/content/drive/MyDrive/anomaly_task2_outputs/run_20251015_181115/ALL_EVENTS.csv`