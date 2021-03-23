def get_id_name_github_dict():
    urls = []
    with open('./github.txt', 'r',) as f1:
        ids = [s.split() for s in f1.readlines()]
        print(ids)
        for id in ids:
            urls.append((id, 'https://github.com/{}/SOFT130002_lab/tree/main/lab0/{}'))


if __name__ == '__main__':
    get_id_name_github_dict()
