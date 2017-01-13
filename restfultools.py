from flask import jsonify

# define statu_dics here
__R200_OK = {'code': 200, 'message': 'OK all right.'}
__R201_CREATED = {'code': 201, 'message': 'All created.'}
__R204_NO_CONTENT = {'code': 204, 'message': 'All deleted.'}
__R400_BAD_REQUEST = {'code': 400, 'message': 'Bad request.'}
__R403_FORBIDDEN = {'code': 403, 'message': 'You can not do this.'}
__R404_NOT_FOUND = {'code': 404, 'message': 'No result matched.'}

R_M200 = {'code': 200, 'message': '%s'}
R_M201 = {'code': 201, 'message': '%s'}
R_M204 = {'code': 204, 'message': '%s'}
R_M400 = {'code': 400, 'message': '%s'}
R_M403 = {'code': 403, 'message': '%s'}
R_M404 = {'code': 404, 'message': '%s'}


def __reflect(statu_dic):
    if statu_dic == R_M200:
        return __R200_OK
    elif statu_dic == R_M201:
        return __R201_CREATED
    elif statu_dic == R_M204:
        return __R204_NO_CONTENT
    elif statu_dic == R_M400:
        return __R400_BAD_REQUEST
    elif statu_dic == R_M403:
        return __R403_FORBIDDEN
    elif statu_dic == R_M404:
        return __R404_NOT_FOUND
    else:
        return __R400_BAD_REQUEST
    # switcher = {
    #     R_M200: __R200_OK,
    #     R_M201: __R201_CREATED,
    #     R_M204: __R204_NOCONTENT,
    #     R_M400: __R400_BADREQUEST,
    #     R_M403: __R403_FORBIDDEN,
    #     R_M404: __R404_NOTFOUND
    # }
    # return switcher.get(statu_dic, __R400_BADREQUEST)


def full_response(status_dict, data):
    return jsonify({'status': __reflect(status_dict), 'data': data})


def status_response(status_dict, msg = ''):
    if msg == '':
        return jsonify({'status': __reflect(status_dict)})
    code = status_dict.get('code')
    message = status_dict.get('message')
    temp = message % msg
    result = {'code': code, 'message': temp}
    return jsonify({'status': result})


def format_string(value):
    if value is None:
        return None
    if value.startswith('"'):
        value = value[1:]
    if value.endswith('"'):
        value = value[:-1]
    return value
