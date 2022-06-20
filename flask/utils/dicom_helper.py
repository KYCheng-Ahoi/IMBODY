# utils/dicom.py

# DICOM standard browser
# https://dicom.innolitics.com/ciods/rt-dose/image-plane/00200037

# For more information about pydicom, see:
# https://pydicom.github.io/pydicom/stable/tutorials/dataset_basics.html
# https://github.com/pydicom/pydicom/issues/1338
import json, sys
from pydicom import dcmread
from pydicom.multival import MultiValue
from pydicom.valuerep import PersonName

def dictify(ds, is_skip_big_bytes = True):
    """Turn a pydicom Dataset into a dict with keys derived from the Element tags.

    Parameters
    ----------
    ds : pydicom.dataset.Dataset
        The Dataset to dictify

    Returns
    -------
    output : dict
    """

    output = dict()

    for elem in ds:
        #if elem.name in ['Pixel Data']:
        #    print(ds.pixel_array)
        if elem.name in ['Window Center', 'Window Width']:
            output[elem.name] = str(elem.value)
        elif elem.VR == 'SQ':
            output[elem.tag] = [dictify(item) for item in elem]
        elif isinstance(elem.value, PersonName):
            output[elem.name] = str(elem.value.decode())
        elif isinstance(elem.value, MultiValue):
            output[elem.name] = str(elem.value)
        elif isinstance(elem.value, bytes):
            if sys.getsizeof(elem.value) > 200 and is_skip_big_bytes:
                print(f'Skipping {elem.tag} {elem.name} {type(elem.value)} {elem.VR}...')
            else:
                output[elem.name] = str(elem.value)
        elif not isinstance(elem.value, (float, int, str, dict, tuple)) and not type(elem.value) is list:
            print(f'Skipping {elem.tag} {elem.name} {type(elem.value)} {elem.VR}...')
        else:
            output[elem.name] = elem.value

    return output

def save_as_json(fpath, header):
    with open(f'{fpath}_header.json', 'w', encoding='utf-8') as f:
        json.dump(header, f, ensure_ascii=False, indent=4)
    print(f"{len(header)} Metadatas: {header}")

def view_dcm(fpath, ds):
    print(ds)
    print("*"*10)
    print(f"File path........: {fpath}")
    print(f"SOP Class........: {ds.SOPClassUID} ({ds.SOPClassUID.name})")

    pat_name = ds.PatientName
    display_name = pat_name.family_name + ", " + pat_name.given_name
    print(f"Patient's Name...: {display_name}")
    print(f"Patient ID.......: {ds.PatientID}")
    print(f"Modality.........: {ds.Modality}")
    print(f"Study Date.......: {ds.StudyDate}")
    print(f"Image size.......: {ds.Rows} x {ds.Columns}")
    print(f"Pixel Spacing....: {ds.PixelSpacing}")

    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")

    # plot the image using matplotlib
    import matplotlib.pyplot as plt
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.show()


if __name__ == '__main__':

    from pydicom.data import get_testdata_file
    fpath = get_testdata_file("CT_small.dcm")
    #fpath = '../tests/test_imgs/2.dcm'

    def get_header(fpath):
        ds = dcmread(fpath, force=True)
        try:
            return dictify(ds)
        except Exception as e:
            print(e)
            return {}
    
    import time
    start = time.process_time()
    ds = dcmread(fpath, force=True)
    end = time.process_time()
    
    view_dcm(fpath, ds)
    save_as_json(fpath, dictify(ds, False))

    print(f'Extract DICOM header: {end - start}s')
