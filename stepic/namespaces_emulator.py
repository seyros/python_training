import logging
import os.path

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-22s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M')


def create(namespaces_list, namespace, parent):
    if namespace not in namespaces_list:
        namespaces_list.append(dict(name=namespace, parent=parent, vars=[]))


def add(namespaces_list, namespace, var):
    for i in namespaces_list:
        if i['name'] == namespace:
            i['vars'].append(var)


def get(namespaces_list, namespace, var):
    namespace_found, var_found, parent = find_var(namespaces_list, namespace, var)
    if not namespace_found:
        print('None')
    else:
        if var_found:
            print(namespace)
        else:
            # если не нашли переменную в указанном пространстве, ищем в родительском
            if not parent:
                # не нашли в указанном namespace и родительского у него нет (это global)
                print('None')
            else:
                while parent and not var_found:
                    pp = parent
                    namespace_found, var_found, parent = find_var(namespaces_list, pp, var)
                    if namespace_found is None:
                        print('None')
                    else:
                        if var_found:
                            print(pp)
                        else:
                            if parent is None:
                                print('None')


def find_var(namespaces_list, namespace, var):
    namespace_found = False
    var_found = False
    for i in namespaces_list:
        if i['name'] == namespace:
            namespace_found = True
            parent = i.get('parent')
            if len(i['vars']) > 0:
                for j in i['vars']:
                    if j == var:
                        var_found = True
                        return namespace_found, var_found, parent
    return namespace_found, var_found, parent


def emulator():
    n = int(input())
    namespaces_list = [dict(name='global', parent=None, vars=[]), ]

    for i in range(n):
        func, namespace, arg = map(str, input().split())
        if func == 'create':
            create(namespaces_list, namespace, arg)
            logger.info(f'namespaces list: {namespaces_list}')
        if func == 'add':
            add(namespaces_list, namespace, arg)
            logger.info(f'namespaces list: {namespaces_list}')
        if func == 'get':
            get(namespaces_list, namespace, arg)
            logger.info(f'namespaces list: {namespaces_list}')


if __name__ == '__main__':
    emulator()
