<script>

  import Router from 'svelte-spa-router'
  import Login from "./routes/Login.svelte"
  import UserCreate from "./routes/UserCreate.svelte"
  import Home from './routes/Home.svelte'
  import Manga from './routes/Manga.svelte'
  import Video from './routes/Video.svelte'
  import Navigation from './components/Navigation.svelte'
  import Test from './routes/Test.svelte'
  const routes = {
    '/': Login,
    '/user-create': UserCreate,
    '/home': Home,
    '/manga': Manga,
    '/video': Video,
    '/test': Test,
  }

</script>


<Navigation />
<Router {routes} />
