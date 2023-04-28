from core.utils.file_utils import parse_zaloqa22


if __name__ == '__main__':
    infile = 'data/e2eqa-train+public_test-v1/zac2022_train_merged_final.json'
    parse_zaloqa22(infile)