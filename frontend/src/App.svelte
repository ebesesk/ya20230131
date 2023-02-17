<script>

  import Router from 'svelte-spa-router'
  import Login from "./routes/Login.svelte"
  import UserCreate from "./routes/UserCreate.svelte"
  import Navigation from './components/Navigation.svelte'
  
  import Manga from './routes/manga/Manga.svelte'
  import Video from './routes/video/Video.svelte'
  import Home from './routes/home/Home.svelte'
  
  const routes = {
    '/': Login,
    '/user-create': UserCreate,
    '/manga': Manga,
    '/video': Video,
    '/home': Home,
  }

</script>


<Navigation />
<Router {routes} />
