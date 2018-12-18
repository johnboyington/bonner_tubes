from mcnp_template import template
from run_mcnp import run_mcnp
from driver import Filter_Job


# this creates a dummy job and produces an imput used for unit testing
job = Filter_Job('HDPE', 1.0, 0, 'In', '')
job.assign_erg('dummystruct', 0, 1, 10)

run_mcnp(job, template, inp_only=True)
