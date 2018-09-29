function setTheme(siteUrl){
	const theme = readCookie('theme') || 'light';

	var lnk = document.createElement('link');
	lnk.type='text/css';
	lnk.href=`${siteUrl}/theme/css/${theme}.css`;
	lnk.rel='stylesheet';
	document.getElementsByTagName('head')[0].appendChild(lnk);
}