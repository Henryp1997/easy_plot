from pltex.types import LabelCfg

def extract_axis_labels(
    xlabel: str | dict | LabelCfg | None,
    ylabel: str | dict | LabelCfg | None,
    default_label_fsize: int,
    current_labels: dict = {"x": None, "y": None}
):
    """ Create a dict of x and y axis labels, handling defaults and different object types """
    axis_labels = {}
    for name, lab_obj in (
        ("x", xlabel),
        ("y", ylabel)
    ):
        if isinstance(lab_obj, LabelCfg):
            pass
        elif isinstance(lab_obj, dict):
            lab_obj = LabelCfg(
                lab_obj.get("label", name),
                lab_obj.get("fontsize", default_label_fsize)
            )
        elif isinstance(lab_obj, str):
            lab_obj = LabelCfg(lab_obj, default_label_fsize)
        elif lab_obj is None:
            attr_label = current_labels[name] # Get existing X or Y axis label
            if attr_label:
                lab_obj = LabelCfg(attr_label, default_label_fsize)
            else:
                axis_labels[name] = None
        else:
            raise TypeError(
                f"Unexpected type for {name}label. Expected str | dict | LabelCfg but got {type(lab_obj)}"
            )

        if lab_obj is not None:
            lab = getattr(lab_obj, "label", name)
            fsize = getattr(lab_obj, "fontsize", default_label_fsize)

            axis_labels[name] = {
                "label": lab, "fontsize": fsize
            }
    return axis_labels
