window.onload = function(){
	function bottomView(){
	var h1 = document.documentElement.clientHeight;//可见区域高度
	var h2 = document.body.clientHeight;//获取body高度
	if (h1 > h2) document.body.style.height = h1 + 'px';
	}
	bottomView();
}