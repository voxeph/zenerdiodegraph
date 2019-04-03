class ScalingType:
    def _init_(self):
        pass


class LargerThan(ScalingType):
    pass


class SmallerThan(ScalingType):
    pass


def scaler(dataset, limit, scale, type=LargerThan):
    new_dataset = []
    if type == LargerThan:
        for i in dataset:
            if i > limit:
                new_dataset.append(i * scale)
            else:
                new_dataset.append(i)

    elif type == SmallerThan:
        for i in dataset:
            if i < limit:
                new_dataset.append(i * scale)
            else:
                new_dataset.append(i)

    else:
        raise TypeError

    return new_dataset
