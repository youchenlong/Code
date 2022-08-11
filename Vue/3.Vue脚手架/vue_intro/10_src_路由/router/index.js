import Vue from "vue"
import VueRouter from "vue-router"
import Home from "../pages/Home"
import About from "../pages/About"
import News from "../pages/News"
import Message from "../pages/Message"

Vue.use(VueRouter)

export default new VueRouter({
    routes: [
        {
            path: '/home',
            component: Home,
            children: [
                {
                    path: 'news',
                    component: News
                },
                {
                    path: 'message',
                    component: Message
                }
            ]
        },
        {
            path: '/about',
            component: About
        }
    ]
})