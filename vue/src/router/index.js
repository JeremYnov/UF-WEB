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
		path      : '/admin/login',
		name      : 'AdminLogin',
		component : () => import('../views/admin/Login.vue')
	},
	{
		path      : '/admin/dashboard',
		name      : 'AdminDashboard',
		component : () => import('../views/admin/Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
	},
	{
		path      : '/admin/restaurant/dashboard',
		name      : 'AdminRestaurantTableDashboard',
		component : () => import('../views/admin/Restaurant-Table-Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
	},
	{
		path      : '/admin/member/dashboard',
		name      : 'AdminMemberTableDashboard',
		component : () => import('../views/admin/Member-Table-Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
	},
	{
		path      : '/admin/current-orders/dashboard',
		name      : 'AdminCurrentOrderTableDashboard',
		component : () => import('../views/admin/Current-Order-Table-Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
	},
	{
		path      : '/admin/history-orders/dashboard',
		name      : 'AdminHistoryOrderTableDashboard',
		component : () => import('../views/admin/History-Order-Table-Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
	},
	{
		path      : '/admin/restaurant/:id/dashboard',
		name      : 'AdminRestaurantDashboard',
		component : () => import('../views/admin/Restaurant-Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
	},
	{
		path      : '/admin/user/:id/dashboard',
		name      : 'AdminUserDashboard',
		component : () => import('../views/admin/User-Dashboard.vue'),
		meta      : {
			requiresAuth : true,
			admin        : true
		}
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
	{
		path      : '/user/profile',
		name      : 'UserProfile',
		component : () => import('../views/user/Profile.vue'),
		meta      : {
			requiresAuth : true
		}
	},
	{
		path      : '/restaurant/dashboard',
		name      : 'RestaurantDashboard',
		component : () => import('../views/restaurant/Dashboard.vue'),
		meta      : {
			requiresAuth : true
		}
	},
	{
		path      : '/restaurant/signup',
		name      : 'RestaurantSignup',
		component : () => import('../views/restaurant/Signup.vue')
	},
	{
		path      : '/restaurant/login',
		name      : 'RestaurantLogin',
		component : () => import('../views/restaurant/Login.vue')
	},
	{
		path      : '/restaurants',
		name      : 'Restaurants',
		component : () => import('../views/restaurant/Restaurants.vue')
	},
	{
		path      : '/restaurant/:id',
		name      : 'Restaurant',
		component : () => import('../views/restaurant/Restaurant.vue')
	},
	{
		path      : '/cart',
		name      : 'ShoppingCart',
		component : () => import('../views/Shopping-cart.vue'),
		meta      : {
			requiresAuth : true
		}
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
		if (JSON.parse(localStorage.getItem('session'))) {
			if (to.matched.some((record) => record.meta.admin)) {
				if (JSON.parse(localStorage.getItem('session')).user.role == 'admin') {
					next();
				} else {
					next({ name: 'Home' });
				}
			} else {
				next();
			}
		} else {
			if (
				to.name == 'AdminDashboard' ||
				to.name == 'AdminRestaurantTableDashboard' ||
				to.name == 'AdminMemberTableDashboard' ||
				to.name == 'AdminCurrentOrderTableDashboard' ||
				to.name == 'AdminHistoryOrderTableDashboard' ||
				to.name == 'AdminRestaurantDashboard' ||
				to.name == 'AdminUserDashboard'
			) {
				next({ name: 'AdminLogin' });
			} else {
				next({ name: 'UserLogin' });
			}
		}
	} else {
		if (JSON.parse(localStorage.getItem('session'))) {
			if (
				to.name == 'UserLogin' ||
				to.name == 'UserSignup' ||
				(to.name == 'AdminLogin' && JSON.parse(localStorage.getItem('session')).user.role == 'member')
			) {
				next({ name: 'Home' });
			} else {
				if (to.name == 'AdminLogin' && JSON.parse(localStorage.getItem('session')).user.role == 'admin') {
					next({ name: 'AdminDashboard' });
				} else {
					next();
				}
			}
		} else {
			next();
		}
	}
});

export default router;
