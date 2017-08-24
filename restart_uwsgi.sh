uwsgi --stop /home/medit_uwsgi.pid
max_loop_time=5
while (($max_loop_time>0))
do
    num_of_uwsgi=$(ps -aux|grep medit_uwsgi |wc -l)
    if (($num_of_uwsgi>1)); then
        echo "medit_uwsgi still occur, please wait until it stops"
        max_loop_time=$(($max_loop_time-1))
        sleep 1s
    else
        echo "medit_uwsgi has stopped"
        break
    fi
done

if (($max_loop_time==0));then
    echo "medit_uwsgi hasn't stopped after I send order to it 5 seconds!, pleasecheck the status of uwsgi, I cannot start it when it is still running):"
else
    echo "I will start medit_uwsgi again:)"
    uwsgi --ini medit_uwsgi.ini
fi
