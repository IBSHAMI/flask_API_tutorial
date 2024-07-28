rm base.txt && rm local.txt && rm dev.txt && rm production.txt
pip-compile base.in && pip-compile local.in && pip-compile dev.in && pip-compile production.in