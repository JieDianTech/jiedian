function setEnglish(bodyString) {
    var result = bodyString;
    result = result.replaceAll('首页', 'Home page');
    result = result.replaceAll('黑萤矿机', 'Black firefly Ms.');
    result = result.replaceAll('黑萤矿池', 'Cloud Node');
    result = result.replaceAll('IPFS资讯', 'IPFS News');
    result = result.replaceAll('关于我们', 'About Us');
    result = result.replaceAll('下载', 'Download');
    result = result.replaceAll('客户端', 'Client');
    result = result.replaceAll('联系我们', 'Contact Us');
    result = result.replaceAll('客服邮箱', 'Customer Service Email');
    result = result.replaceAll('客服QQ', 'QQ for Customer Service');
    result = result.replaceAll('客服微信', 'WeChat for Customer Service');
    result = result.replaceAll('黑萤科技产品顾问', 'Product Consultant');
    result = result.replaceAll('黑萤科技官方服务号', 'Service Number');
    result = result.replaceAll('登录', 'Login');
    result = result.replaceAll('退出登录', 'logout');
    result = result.replaceAll('注册', 'Register');
    result = result.replaceAll('多语言', 'Language');
    return result;
}

function setFanti(bodyString) {
    var result = bodyString;
    result = result.replaceAll('首页', '首頁');
    result = result.replaceAll('黑萤矿机', '黑螢礦機');
    result = result.replaceAll('黑萤矿池', '黑螢礦池');
    result = result.replaceAll('IPFS资讯', 'IPFS資訊');
    result = result.replaceAll('关于我们', '關於我們');
    result = result.replaceAll('下载', '下載');
    result = result.replaceAll('客户端', '客戶端');
    result = result.replaceAll('联系我们', '聯系我們');
    result = result.replaceAll('客服邮箱', '客服郵箱');
    result = result.replaceAll('客服QQ', '客服QQ');
    result = result.replaceAll('客服微信', '客服微信');
    result = result.replaceAll('黑萤科技产品顾问', '黑螢科技產品顧問');
    result = result.replaceAll('黑萤科技官方服务号', '黑螢科技官方服務號');
    result = result.replaceAll('登录', '登入');
    result = result.replaceAll('退出登录', '退出登入');
    result = result.replaceAll('注册', '註冊');
    result = result.replaceAll('多语言', '多語言');
    return result;
}