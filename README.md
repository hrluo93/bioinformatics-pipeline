# bioinformatics-pipline
1. infer Nc SNP Heterozygous rate by Maximum Likelihood Estimate(MLE).py
Need to input sequenced individuals mean of Heterozygous rate, standard deviation of Heterozygous rate and census pop size(Nc)
the infered snp Heterozygous distribution set as Normal distribution x = μ + σ * np.random.randn(nc)
result:(Nc's mean of Heterozygous rate, Nc's standard deviation of Heterozygous rate)

2. Genome Assembly, Polish, and Annotation

Canu/Flye+Racon+Pilon+EDTA+Repeatmasker+braker2
1. Nanopore/PB seq to Assembly
2. 250bp PE and 10K PE lib to Polish
3. 150bp bp PE lib RNA-seq to Annotation by using augustus in braker2
