(function() {
	var posts = document.getElementById('home-page__post-list');
	var homePage = document.getElementById('home-page');
	var clickListener = posts.addEventListener('click', function(e) {
		var link = e.target;
		var targetIsLink = link.classList.contains('link');
		var fetchLink = link.getAttribute('data-fetch') || 'true';
		var title;
		var url;

		if(targetIsLink === true && fetchLink !== 'false') {
			try {
				title = link.getAttribute('title');
				url = link.href;
				history.pushState(null, title, url);
				e.preventDefault();
				e.stopPropagation();
				ajax({
					url: url,
					method: 'GET',
					success: function(response) {
						var div = document.createElement('div');
						var content;

						div.innerHTML = response;
						content = div.getElementsByClassName('post-page')[0];
						homePage.innerHTML = content.innerHTML;
						homePage.classList.add('fade-in');

					},
					error: function(response) {
						link.setAttribute('data-fetch', false)
						link.click();
					}
				});
			}
			catch(e) {
				link.setAttribute('data-fetch', false);
			}
		}
	});
}());