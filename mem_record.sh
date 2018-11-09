cp /home/ligang/mem_stat.log /home/ligang/tmp1
head -n 14 /tmp/mem_stat_front_merge > /home/ligang/tmp2
cat /home/ligang/tmp1 /home/ligang/tmp2 > /home/ligang/mem_stat.log
rm /home/ligang/tmp*
