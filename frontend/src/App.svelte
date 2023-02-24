<script>

  import Router from 'svelte-spa-router'
  import Login from "./routes/Login.svelte"
  import UserCreate from "./routes/UserCreate.svelte"
  import Navigation from './components/Navigation.svelte'
  
  import Manga from './routes/manga/Manga.svelte'
  // import Video from './routes/video/Video.svelte'
  import Video from './routes/video/Video.svelte'
  import Realestate from './routes/realestate/Realestate.svelte'
  import Worked from './routes/worked/Worked.svelte'
  
  const routes = {
    '/': Login,
    '/user-create': UserCreate,
    '/manga': Manga,
    // '/video': Video,
    '/video': Video,
    '/realestate': Realestate,
    '/worked': Worked
  }

</script>


<Navigation />
<Router {routes} />
