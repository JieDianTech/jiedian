
//登录信息
var userId = getCookie("logintime");
var userName = getCookie("username");
if (userName == null) {
    userName = "";
}

//或取页面传值
function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}

//写cookies
function setCookie(name, value) {
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = name + "=" + encodeURI(value) + ";expires=" + exp.toGMTString();
}
//读取cookies
function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return decodeURI(arr[2]);
    else
        return null;
}
//删除cookies
function delCookie(name) {
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval = getCookie(name);
    if (cval != null)
        document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString();
}

//為系統追加replaceAll方法
String.prototype.replaceAll = function (oldStr, newStr) {
    return this.replace(new RegExp(oldStr, "gm"), newStr);
}

////自动检测文本域是否是数字，正则剔除非数字/////
function clearNoNum(obj) {
    //先把非数字的都替换掉，除了数字和.
    obj.value = obj.value.replace(/[^\d.]/g, "");
    //必须保证第一个为数字而不是.
    obj.value = obj.value.replace(/^\./g, "");
    //保证只有出现一个.而没有多个.
    obj.value = obj.value.replace(/\.{2,}/g, ".");
    //保证.只出现一次，而不能出现两次以上
    obj.value = obj.value.replace(".", "$#$").replace(/\./g, "").replace("$#$", ".");

    var arr = obj.value.split('.');
    if (arr.length > 1) {
        //最大10亿
        if (arr[0].length > 11) {
            obj.value = obj.value.substring(0, obj.value.length - 1);
        }
    } else {
        //最大10亿
        if (arr[0].length > 11) {
            obj.value = obj.value.substring(0, obj.value.length - 1);
        }
    }
}

//获取验证码
function getCode(ph) {
    var param = {};
    var account = ph == "login" ? $("#login_phone").val() : $("#register_phone").val();
    
    if (account == "") {
        layer.alert('请输入手机号//邮箱地址！', { icon: 2 });
        return;
    }
    var regMobile = /^1[23456789]\d{9}$/;
    var regEmail = /^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$/;
    var reg = /[@]/gi;
    if (reg.test(account)) {
        if (!regEmail.test(account)) {
            layer.alert('请输入正确的邮箱', { icon: 2 });
            return;
        }
        param.phone = "";
        param.email = account;
    } else {
        if (!regMobile.test(account)) {
            layer.alert('请输入正确的手机号', { icon: 2 });
            return;
        }
        param.phone = account;
        param.email = "";
    }

    var flag = false;
    if (ph == "login") {
        $.ajax({
            type: "POST",
            url: "/Account/Exist",
            data: param,
            datatype: "json",
            success: function (res) {
                if (res.code == 0) {
                    layer.alert('您还没有注册，请先注册！', { icon: 2 })
                } else {
                    getYZM(param, "login_code_but");
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                layer.alert('请求错误', { icon: 2 });
            }
        });
    } else {
        $.ajax({
            type: "POST",
            url: "/Account/Exist",
            data: param,
            datatype: "json",
            success: function (res) {
                if (res.code == 1) {
                    layer.alert('您的手机号/邮箱已注册，请登录！', { icon: 2 })
                } else {
                    getYZM(param, "register_code_but");
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                layer.alert('请求错误！', { icon: 2 });
            }
        });
    }
}

function getYZM(param, val) {
    $.ajax({
        type: "POST",
        url: "/Account/GetCode",
        data: param,
        datatype: "json",
        success: function (res) {
            settime(val);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            layer.alert('请求错误！', { icon: 2 });
        }
    });
}

var countdown = 60;
function settime(obj) {
    var _generate_code = $("#" + obj);
    if (countdown == 0) {
        _generate_code.attr("disabled", false);
        _generate_code.val("获取验证码");
        countdown = 60;
        return false;
    } else {
        _generate_code.attr("disabled", true);
        _generate_code.val("重新发送(" + countdown + ")");
        countdown--;
    }
    setTimeout(function () {
        settime(obj);
    }, 1000);
}




//弹出登录框
function show_login() {
    close_register(); //关闭注册框
    $('.login-mask').show();
    $('.login-mask').height($(document).height());
    $('.login-popover').slideDown(200);
}
//关闭登录框
function close_login() {
    $('.login-mask').hide();
    $('.login-popover').slideUp(200);
}

//弹出注册框
function show_register() {
    close_login(); //关闭登录框
    $('.register-mask').show();
    $('.register-mask').height($(document).height());
    $('.register-popover').slideDown(200);
}
//关闭注册框
function close_register() {
    $('.register-mask').hide();
    $('.register-popover').slideUp(200);
}