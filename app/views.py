# -*- coding:utf-8 -*-
import restfultools
from app import app, db, models, request
from restfultools import *
import time


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'

__results = []

'''
控件类别
'''


# 增加控件类别
# type 类别名称
@app.route('/simpleCode/api/v1.0/weightList/add')
def add_weight():
    weight_type = format_string(request.args.get('type'))
    if weight_type is None:
        return status_response(R_M400, 'Type is not available!')
    weights = models.WeightList.query.all()
    weight = models.WeightList(name=weight_type)
    for w in weights:
        if w.name == weight_type:
            return status_response(R_M404)
    db.session.add(weight)
    db.session.commit()
    __results.clear()
    __results.append(weight.__repr__())
    return full_response(R_M200, __results)


# # 删除控件类别
# # id 类别id
# @app.route('/simpleCode/api/v1.0/weightList/delete')
# def delete_weight():
#     type_id = format_string(request.args.get('id'))
#     if type_id is None:
#         return status_response(R_M400, 'Id is not available!')
#     weights = models.WeightList.query.all()
#     for w in weights:
#         if str(w.id) == type_id:
#             # weights = db.session.query(models.WeightList).filter_by(id=w.id)
#             # temp_arr = []
#             # for temp in weights:
#             #     temp_arr.append(temp.__repr__())
#             # if len(temp_arr) > 0:
#             #     return restfultools.status_response(restfultools.R_M400, '请先将该类别下的详情数据清空!')
#             db.session.delete(w)
#             db.session.commit()
#             return restfultools.status_response(restfultools.R_M200, 'Delete Success')
#     return restfultools.status_response(restfultools.R_M404)


# 删除控件类别以及其下控件详情
# id 类别id
@app.route('/simpleCode/api/v1.0/weightList/delete')
def delete_weight_force():
    type_id = format_string(request.args.get('id'))
    if type_id is None:
        return status_response(R_M400, 'Id is not available!')
    weights = models.WeightList.query.all()
    for w in weights:
        if str(w.id) == type_id:
            weights = db.session.query(models.WeightDetail).filter_by(base_id=w.id)
            for temp in weights:
                db.session.delete(temp)
                db.session.commit()
            db.session.delete(w)
            db.session.commit()
            return restfultools.status_response(restfultools.R_M200, 'Delete Success')
    return restfultools.status_response(restfultools.R_M404)


# 更新控件类别
# id 类别id
# new_type 更改后类别名称
@app.route('/simpleCode/api/v1.0/weightList/update')
def update_weight():
    type_id = format_string(request.args.get('id'))
    if type_id is None:
        return status_response(R_M400, 'Id is not available!')
    new_type = format_string(request.args.get('new_type'))
    if new_type is None:
        return status_response(R_M400, 'New_type is not available!')
    weights = db.session.query(models.WeightList).filter_by(id=type_id)
    for w in weights:
        if str(w.id) == type_id:
            w.name = new_type
            db.session.commit()
            __results.clear()
            __results.append(w.__repr__())
            return full_response(R_M200, __results)
    return status_response(R_M404)


# 查找所有控件类别
@app.route('/simpleCode/api/v1.0/weightList/query')
def query_all():
    __results.clear()
    weights = models.WeightList.query.all()
    for w in weights:
        __results.append(w.__repr__())
    return full_response(R_M200, __results)


'''
控件详情
'''


# 增加控件详情
# id 类别id
# code 详情代码
@app.route('/simpleCode/api/v1.0/weightDetail/add')
def add_weight_detail():
    parent_id = format_string(request.args.get('id'))
    if parent_id is None:
        return status_response(R_M400, 'Id is not available!')
    code = format_string(request.args.get('code'))
    if code is None:
        return status_response(R_M400, 'Code is not available!')
    weights = models.WeightList.query.all()
    for w in weights:
        if str(w.id) == parent_id:
            weight = models.WeightDetail(code=code, base_id=parent_id, create_time=time.time())
            print(code)
            print(parent_id)
            print(time.time())
            db.session.add(weight)
            db.session.commit()
            __results.clear()
            __results.append(weight.__repr__())
            return full_response(R_M200, __results)
    return status_response(R_M404, 'No such parent id.')


# 删除控件详情
# id 控件id
@app.route('/simpleCode/api/v1.0/weightDetail/delete')
def delete_weight_detail():
    weight_id = format_string(request.args.get('id'))
    if weight_id is None:
        return status_response(R_M400, 'Id is not available!')
    weights = models.WeightDetail.query.all()
    for w in weights:
        if str(w.id) == weight_id:
            db.session.delete(w)
            db.session.commit()
            return restfultools.status_response(restfultools.R_M200, 'Delete Success')
    return restfultools.status_response(restfultools.R_M404)


# 更新控件详情
# id 控件id
# code 控件代码
@app.route('/simpleCode/api/v1.0/weightDetail/update')
def update_weight_detail():
    weight_id = format_string(request.args.get('id'))
    if weight_id is None:
        return status_response(R_M400, 'Id is not available!')
    code = format_string(request.args.get('code'))
    if code is None:
        return status_response(R_M400, 'Code is not available!')
    weights = db.session.query(models.WeightDetail).filter_by(id=weight_id)
    for w in weights:
        if str(w.id) == weight_id:
            w.code = code
            db.session.commit()
            __results.clear()
            __results.append(w.__repr__())
            return full_response(R_M200, __results)
    return status_response(R_M404)


# 查找类别下所有控件详情
# id 类别id
@app.route('/simpleCode/api/v1.0/weightDetail/query')
def query_all_detail():
    parent_id = format_string(request.args.get('id'))
    if parent_id is None:
        return status_response(R_M400, 'Id is not available!')
    weights = models.WeightList.query.all()
    temp = []
    for w in weights:
        if str(w.id) == parent_id:
            temp.append(w.id)
            break
    if len(temp) == 0:
        return status_response(R_M400, 'No such parent id!')
    weights = db.session.query(models.WeightDetail).filter_by(base_id=parent_id)
    __results.clear()
    for w in weights:
        __results.append(w.__repr__())
    return full_response(R_M200, __results)


# # 查找类别下所有控件详情
# # id 类别id
# @app.route('/simpleCode/api/v1.0/weightDetail/queryAll')
# def query_all_detail_ss():
#     __results.clear()
#     weights = models.WeightDetail.query.all()
#     for w in weights:
#         __results.append(w.__repr__())
#     return full_response(R_M200, __results)


