import pandas as pd

# Query a IRMA code from code list
def get_irma_code(code): 
    seg = code.split('-')
    a = get_irma_code_seg("archieve/A_technical_code.csv", seg[0])
    b = get_irma_code_seg("archieve/B_directional_code.csv", seg[1])
    c = get_irma_code_seg("archieve/C_anatomical_code.csv", seg[2])
    d = get_irma_code_seg("archieve/D_biological_code.csv", seg[3])
    return f"{a}|{b}|{c}|{d}"

def get_irma_code_seg(filename, code):
    if code.isdigit():
        code = int(code)
        tree_codes = [int(str(code)[:(x+1)]) for x in range(len(str(code)))]
    else:
        tree_codes = code
    df = pd.read_csv(filename, delimiter = ",", header=None, names=['code', 'text'])
    df['code'] = df['code'].astype(str)
    # print(df)
    def get_text(x):
        try:
            return df.loc[df['code'] == str(x)]['text'].values[0]
        except:
            return
    description = ','.join(list(filter(None, map(get_text, tree_codes))))
    return description

if __name__=='__main__':
    print(get_irma_code_seg("archieve/A_technical_code.csv", "1120"))
    print(get_irma_code("1121-110-411-700"))
