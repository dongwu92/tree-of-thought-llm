import sys
import argparse
import socks, socket

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10809)
socket.socket = socks.socksocket

sys.path.insert(0, 'src/')

from tot.args import save_args

args = argparse.Namespace(
    backend='gpt-4-1106-preview', 
    temperature=0.7, 
    task='game24', 
    naive_run=False, 
    prompt_sample=None, 
    method_generate='propose', 
    method_evaluate='value', 
    method_select='greedy', 
    n_generate_sample=1, 
    n_evaluate_sample=3, 
    n_select_sample=5
)
save_args(args)


from tot.models import gpt_usage
from tot.methods.bfs import solve
from tot.tasks.game24 import Game24Task

task = Game24Task()
ys, infos = solve(args, task, 1000)
print('++++>', ys[0])
print('usage_so_far', gpt_usage(args.backend))

from tot.prompt_cache import pcache
pcache.save()