# test_cloud_api.py  —— 用 pytest 跑：pytest test_cloud_api.py -v
import requests

def test_resource_status():
    # 调用云平台类接口，校验状态码（对应"云资源创建/销毁"验证）
    resp = requests.get("https://httpbin.org/status/200", timeout=5)
    assert resp.status_code == 200

def test_create_resource():
    # 模拟"创建算力资源"，校验返回体与入参一致（对应"AI算力任务下发"）
    payload = {"name": "test-gpu", "gpu": 1}
    resp = requests.post("https://httpbin.org/post", json=payload, timeout=5)
    assert resp.status_code in (200, 201)
    assert resp.json()["json"]["name"] == "test-gpu"

# 面试讲：脚本辅助测试 = 把重复接口验证自动化，
# 覆盖正常/异常(错误码)/边界(超大参数)，比手工稳、可回归。

def test_error_status():
    payload = {"name": "test-gpu", "gpu": 1}
    resp = requests.post("https://httpbin.org/post", json=payload, timeout=5)
    assert resp.status_code in (200, 404)
    assert resp.json()["json"]["name"] == "test-gpu"

def test_error_status():
    """异常场景：访问不存在的资源，期望返回 404"""
    resp = requests.get("https://httpbin.org/status/404", timeout=5)
    assert resp.status_code == 404   # 明确期望：资源不存在就是 404
