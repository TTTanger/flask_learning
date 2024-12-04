document.addEventListener('DOMContentLoaded', function() {
  // 初始化页面
  initPage();

  // 绑定导航链接的点击事件
  bindNavLinks();

  window.onload = function() {
    var body = document.getElementById('login');
    body.className = 'login-style'; // 应用预定义的类
};
  // 确保在 DOM 完全加载后绑定关闭模态框的事件
  const closeButton = document.querySelector('.close');
  if (closeButton) {
    closeButton.addEventListener('click', closeModal);
  } 

  // 点击模态框外部关闭
  window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
      closeModal();
    }
  };

  document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // 阻止表单默认提交行为
  
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
  
    // 简单的身份验证逻辑
    if (username === 'zjy' && password === 'zjysdmn') {
      document.getElementById('message').innerText = '真聪明！';
      document.getElementById('message').style.color = 'green';
      localStorage.setItem('isLoggedIn', 'true'); // 设置登录状态
      setTimeout(function() { loadPage("index"); }, 2000); // 2秒后重定向
  } else {
      document.getElementById('message').innerText = '你猜是啥？';
      document.getElementById('message').style.color = 'red';
  }
    });
  // // 设置用户名
  // if (!localStorage.getItem("name")) {
  //   setUserName();
  // } else {
  //   let storedName = localStorage.getItem("name");
  //   setWelcomeMessage(storedName);
  // }
});

function initPage() {
  console.log('Page initialized');
}

function bindNavLinks() {
  const navLinks = document.querySelectorAll('nav a');

  navLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.preventDefault(); // 阻止默认的链接跳转行为

      const targetPage = this.getAttribute('href').slice(1); // 获取目标页面名称
      loadPage(targetPage);
    });
  });
}

// let myButton = document.querySelector("button");

function setWelcomeMessage(username) {
  const welcomeMessage = `Hello, ${username}`;
  const currentPath = window.location.pathname;

  let headingElement;

  if (currentPath.endsWith('index.html')) {
    headingElement = document.getElementById("home_h1");
  } 
  if (headingElement) {
    headingElement.textContent = welcomeMessage;
  }
}

/*
function setUserName() {
  let myName = prompt("Plz enter your name:")

  if (myName && myName.trim()) { // 检查用户是否输入了有效的名字
    localStorage.setItem("name", myName.trim());
    setWelcomeMessage(myName.trim());
  } else {
    alert("Name cannot be empty. Please try again.");
    setUserName(); // 如果名字无效，重新提示用户输入
  }
}

// myButton.onclick = function () {
//   setUserName();
// };
*/

// 根据页面名称加载对应的内容
function loadPage(page) {
  switch (page) {
    case 'login':
      window.location.href = 'login.html';
      break;
    case 'index':
      window.location.href = 'index.html';
      break;
    case 'notes':
      window.location.href = 'notes.html';
      break;
    case 'albums':
      window.location.href = 'albums.html';
      break;
    default:
      console.error('Unknown page:', page);
  }
}
