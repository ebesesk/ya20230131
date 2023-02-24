<script>
  import { link } from 'svelte-spa-router'
  import {page, keyword, access_token, username, is_login, mangaKeyword, mangaPage } from '../lib/store'

</script>

<nav class="navbar navbar-expand-sm navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="/"
       on:click={() => {
         $access_token = ''
         $username=''
         $is_login=false
       }}>
      햣
      {#if $is_login}
      LogOut
      {/if}
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
      <ul class="navbar-nav">
        {#if $is_login}
        <li class="nav-item">
          <a use:link class="nav-link" aria-current="page" href="/worked">출근부</a>
        </li>
        <li class="nav-item">
          <a use:link class="nav-link" aria-current="page" href="/realestate">부동산</a>
        </li>

        <li class="nav-item">
          <a use:link class="nav-link" aria-current="page" href="/video">video</a>
        </li>
        
        <li class="nav-item dropdown">
          <a use:link class="nav-link dropdown-toggle" href="/manga" id="navbarDropdownMenuLinkmanga" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            만화
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLinkmanga">
            <li><a use:link class="dropdown-item" href="/manga"
                >
                all</a></li>
            <li><a use:link class="dropdown-item" href="/manga">추천</a></li>
            <li><a use:link class="dropdown-item" href="/manga">짧은거</a></li>
          </ul>
        </li>
        {:else}
        <li class="nav-item">
          <a use:link class="nav-link active" aria-current="page" href="/">로그인</a>
        </li>
        {/if}
      </ul>
    </div>
  </div>
</nav>

<style>
  /* .navbar.navbar-expand-sm {
  } */
  /* .container {
    display: flex;
    justify-items: flex-end;
    justify-content: flex-end;
  } */
  .dropdown-item {
    justify-self: flex-end;
  }
</style>