import argparse
import sys
import parse_sql_script
import os
import worker
import shutil
import pickle

def main(src_lang, target_lang, src_ll_sql, out_dir, overwrite=False):
    print('source language:', src_lang)
    print('target language:', target_lang)
    print('source language links sql file', src_ll_sql)
    print('output directory', out_dir)
    print('Force overwrite', args.overwrite)
    
    df_path = os.path.join(output_dir, '{}_{}_langlinks'.format(src_lang, target_lang))

    if os.path.exists(df_path):
        if overwrite:
            shutil.rmtree(out_dir)
        else:
            raise ValueError

    if not os.path.exists(out_dir): 
        os.makedirs(out_dir)


    src_df = parse_sql_script.sql2df(src_ll_sql, target_lang)

    print("inter-language links sql file loaded successfully")
    pickle.dump(src_df, open(df_path, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)



parser = argparse.ArgumentParser(description='Align Wikipedia documents based on interlanguage links .')

parser.add_argument('--src-lang', type=str, help='source language. '
                                                'e.g., ar for Arabic, '
                                                'en for English, or '
                                                'fr for French ...', required=True)
parser.add_argument('--tgt-lang', type=str, help='target language. '
                                                   'e.g., ar for Arabic, '
                                                   'en for English, or '
                                                   'fr for French ...', required=True)
parser.add_argument('--sql-file', type=str, help='source language links sql file. '
                                                'Obtained from https://dumps.wikimedia.org/', required=True)
parser.add_argument('--out-dir', type=str, help='the output directory.', required=True)
parser.add_argument('--overwrite', action='store_true')

if __name__ == '__main__':
    args = parser.parse_args()
    src_lang = args.src_lang
    target_lang = args.tgt_lang
    src_ll_sql = args.sql_file
    out_dir = args.out_dir
    main(src_lang, target_lang, src_ll_sql, out_dir, args.overwrite)


