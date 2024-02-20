from collections import OrderedDict
from typing import List


class Average(object):
    """Computes and stores the average and current value"""
    def __init__(self, fmt='f', with_last=False):
        self.fmt = fmt
        self.reset()
        if with_last:
            self.fmtstr = '{avg:' + self.fmt + '}({val:' + self.fmt + '})'
        else:
            self.fmtstr = '{avg:' + self.fmt + '}'

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count
    
    def __len__(self):
        return self.count
    
    def average(self):
        return self.avg if self.count else None
    
    def empty(self):
        return self.count == 0

    def __str__(self):
        return self.fmtstr.format(**self.__dict__)


class AverageMeter(object):
    def __init__(self, names:List[str]=[], prefix="", val_sep=' ', name_sep=':', **kwargs):
        self.meters = OrderedDict()
        for name in set(names):
            self.meters[name] = Average(**kwargs)

        self.prefix = prefix
        self.val_sep = val_sep
        self.name_sep = name_sep
    
    def reset(self):
        for key in self.meters.keys():
            self.meters[key].reset()

    def push(self, name, **kwargs):
        if name not in self.meters.keys():
            self.meters[name] = Average(**kwargs)
    
    def __setitem__(self, name, value: Average):
        assert isinstance(value, Average), "make sure set {type(value) is Average}"
        self.meters[name] = value

    def __getitem__(self, name):
        return self.meters[name]
    
    def update(self, name_dict, count=1):
        for name, value in name_dict.items():
            self.meters[name].update(value, n=count)

    def __str__(self):
        if self.prefix != '':
            entries = [self.prefix]
        else:
            entries = []
            
        entries += [f"{name}{self.name_sep}"+str(meter) for name, meter in self.meters.items() if not meter.empty()]
        show = self.val_sep.join(entries)
        return show