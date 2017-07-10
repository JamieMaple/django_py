window.onload = function(){
	function bottomView(){
	var h1 = document.documentElement.clientHeight;//可见区域高度
	var h2 = document.body.clientHeight;//获取body高度
	if (h1 > h2) document.body.style.height = h1 + 'px';
	}
	bottomView();

	particlesJS('particle-js',
			  {
			  "particles": {
			    "number": {
			      "value": 100,
			      "density": {
			        "enable": true,
			        "value_area": 800
			      }
			    },
			    "color": {
			      "value": "#abcdef"
			    },
			    "shape": {
			      "type": "circle",
			      "stroke": {
			        "width": 0,
			        "color": "#000000"
			      },
			      "polygon": {
			        "nb_sides": 5
			      },
			      "image": {
			        "src": "img/github.svg",
			        "width": 100,
			        "height": 100
			      }
			    },
			    "opacity": {
			      "value": 0.5,
			      "random": false,
			      "anim": {
			        "enable": false,
			        "speed": 0.5594405594405595,
			        "opacity_min": 0.1,
			        "sync": false
			      }
			    },
			    "size": {
			      "value": 3,
			      "random": true,
			      "anim": {
			        "enable": false,
			        "speed": 40,
			        "size_min": 0.1,
			        "sync": false
			      }
			    },
			    "line_linked": {
			      "enable": true,
			      "distance": 150,
			      "color": "#a7a7a7",
			      "opacity": 0.4,
			      "width": 1
			    },
			    "move": {
			      "enable": true,
			      "speed": 2,
			      "direction": "none",
			      "random": true,
			      "straight": false,
			      "out_mode": "out",
			      "bounce": false,
			      "attract": {
			        "enable": false,
			        "rotateX": 600,
			        "rotateY": 1200
			      }
			    }
			  },
			  "interactivity": {
			    "detect_on": "canvas",
			    "events": {
			      "onhover": {
			        "enable": true,
			        "mode": "grab"
			      },
			      "onclick": {
			        "enable": true,
			        "mode": "bubble"
			      },
			      "resize": true
			    },
			    "modes": {
			      "grab": {
			        "distance": 95.90409590409591,
			        "line_linked": {
			          "opacity": 1
			        }
			      },
			      "bubble": {
			        "distance": 100,
			        "size": 5,
			        "duration": 0.5,
			        "opacity": 0.2761062521824573,
			        "speed": 3
			      },
			      "repulse": {
			        "distance": 200,
			        "duration": 0.4
			      },
			      "push": {
			        "particles_nb": 4
			      },
			      "remove": {
			        "particles_nb": 2
			      }
			    }
			  },
			  "retina_detect": true
			}

			);
}