cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2" "$1}'
grep -P "^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$" file.txt
python3 -c 'print("\n".join(map(" ".join,zip(*map(str.split,open("file.txt").readlines())))))'
awk '
    {

        for (i=1; i<=NF; ++i) {

            if (1==NR) {

                ans[i]=$i;
            } else {

                ans[i]=ans[i]" "$i;
            }
        }        
    } END {

        for (j=1; j<=NF; ++j) {

            print ans[j];
        }
    }
' file.txt
awk 'NR == 10' file.txt
sed -n 10p file.txt
tail -n+10 file.txt|head -1



