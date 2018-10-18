function setTheme(siteUrl, theme){
	// var lnk = document.createElement('link');
	// lnk.id='theme-css'
	// lnk.type='text/css';
	// lnk.href=`${siteUrl}/theme/css/${theme}.css`;
	// lnk.rel='stylesheet';
	// document.getElementsByTagName('head')[0].appendChild(lnk);
	// createCookie('theme', theme);
	const linkTags = document.getElementsByTagName("link");
	for(var i = 0; i<linkTags.length; i++){
		if(linkTags[i] && 
			linkTags[i].rel.indexOf("stylesheet") !== -1 && 
			linkTags[i].title ){
			linkTags[i].disabled = true;
		}
		if(linkTags[i] && linkTags[i].title === theme) {
			linkTags[i].disabled = false;
		}
	}
	createCookie('theme', theme, 365);
}

function changeTheme(siteUrl, theme) {
	document.getElementById('theme-css').href = `${siteUrl}/theme/css/${theme}.css`;
}