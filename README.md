# xmeter
> summary average meter


## usage

```python
from summary import Average, AverageMeter


if __name__ == '__main__':
    meter = AverageMeter(names=['loss', 'acc'], sep=',', name_sep='=', fmt='.4f', with_last=True)
    meter['dloss'] = Average(fmt='.2f', with_last=False)

    meter.update({'loss': 0.5, 'acc': 5.1})
    meter['loss'].update(0.6)
    meter['acc'].update(0.2)
    meter['dloss'].update(0.8, n=2)

    print(meter)
```