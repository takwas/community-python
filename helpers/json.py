from playhouse.shortcuts import model_to_dict


def models_to_dict(models):
    dict = []

    for m in models:
        dict.append(model_to_dict(m))

    return dict