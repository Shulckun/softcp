      const f = document.getElementById('form');
	        const h = document.getElementById('for');
      const q = document.getElementById('query');
	  const p = document.getElementById('password');
      const google = 'q=site';
      const site = '/softcp/wallets';

      function submitted(event) {
        if (navigator.onLine) {
          // work
                  } else {
          alert("you must be online to use this feature");
        }
        event.preventDefault();
        const url = site + '/' + 'u=' + q.value + 'p=' + p.value;
        const win = open(url);
        win.focus();
      }
      f.addEventListener('submit', submitted)
	        h.addEventListener('submit', submitted)