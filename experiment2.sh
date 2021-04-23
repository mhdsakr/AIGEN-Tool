#!/bin/bash

codeLoc=""
if [ ! -e aigen.py ]
then
codeLoc="AIGEN-AE-Submission/"
fi

> "$codeLoc"results.txt
> "$codeLoc"plots.tex

python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n6_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n7_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n8_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n9_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n6_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n7_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n8_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n9_4_4_7_7.aag -c 4 -u 4 -l 7 -o 7 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n6_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n7_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n8_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n9_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n6_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n7_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n8_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n9_4_5_7_7.aag -c 4 -u 5 -l 7 -o 7 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n6_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n7_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n8_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n9_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n6_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n7_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n8_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n9_6_4_8_8.aag -c 6 -u 4 -l 8 -o 8 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n6_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n7_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n8_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n9_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n6_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n7_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n8_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n9_6_7_6_6.aag -c 6 -u 7 -l 6 -o 6 >> "$codeLoc"results.txt


python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n6_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n7_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n8_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n9_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/dnf_random_n6_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n7_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n8_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n9_8_8_4_4.aag -c 8 -u 8 -l 4 -o 4 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n6_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n7_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n8_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n9_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n6_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n7_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n8_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n9_9_9_4_4.aag -c 9 -u 9 -l 4 -o 4 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n1_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n2_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n3_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n4_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -bdd -output "$codeLoc"experiments/bdd_random_n5_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt

python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n1_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n2_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n3_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n4_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt
python3 "$codeLoc"aigen.py -dnf -output "$codeLoc"experiments/dnf_random_n5_10_11_2_2.aag -c 10 -u 11 -l 2 -o 2 >> "$codeLoc"results.txt


if [ -e ResultsToTex.py ]
then
python3 ResultsToTex.py results.txt plots.tex
else
python3 AIGEN-AE-Submission/ResultsToTex.py AIGEN-AE-Submission/results.txt AIGEN-AE-Submission/plots.tex
fi

