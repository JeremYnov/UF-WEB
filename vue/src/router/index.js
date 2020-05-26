import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
	{
		path      : '/',
		name      : 'Home',
		component : Home
	},
	{
		path      : '/about',
		name      : 'About',
		component : () => import('../views/About.vue')
	},
	{
		path      : '/user/signup',
		name      : 'UserSignup',
		component : () => import('../views/user/Signup.vue')
	},
	{
		path      : '/user/login',
		name      : 'UserLogin',
		component : () => import('../views/user/Login.vue')
	},
	{
		path      : '/user/logout',
		name      : 'UserLogout',
		component : () => import('../views/user/Logout.vue'),
		meta      : {
			requiresAuth : true
		}
	},
	// {
	// 	path      : '/admin/signup',
	// 	name      : 'AdminSignup',
	// 	component : () => import('../views/admin/Signup.vue')
	// },
	{
		path      : '/restaurant/signup',
		name      : 'RestaurantSignup',
		component : () => import('../views/restaurant/Signup.vue')
	},
	{
		path      : '*',
		name      : 'Error404',
		component : () => import('../views/error/404.vue')
	}
];

const router = new VueRouter({
	mode   : 'history',
	base   : process.env.BASE_URL,
	routes
});

router.beforeEach((to, from, next) => {
	if (to.matched.some((record) => record.meta.requiresAuth)) {
		console.log('aaaaaa');
		console.log(JSON.parse(localStorage.getItem('session')));

		if (JSON.parse(localStorage.getItem('session'))) {
			console.log('bbbbbb');

			next();
		} else {
			console.log('cccccc');

			next({ name: 'UserLogin' });
		}
	} else {
		if (JSON.parse(localStorage.getItem('session'))) {
			if (to.name == 'UserLogin') {
				next({ name: 'About' });
			} else if (to.name == 'UserSignup') {
				next({ name: 'About' });
			} else {
				next();
			}
		} else {
			next();
		}
	}
});

export default router;
