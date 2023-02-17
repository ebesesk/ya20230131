<script>
  import { link } from 'svelte-spa-router'
  import {page, keyword, access_token, username, is_login, mangaKeyword, mangaPage } from '../lib/store'

</script>

<nav class="navbar navbar-expand-sm navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="/">햣</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a use:link class="nav-link" aria-current="page" href="/home">Home</a>
        </li>
        {#if $is_login}
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
        <li class="nav-item dropdown">
          <a use:link class="nav-link dropdown-toggle" href="/video" id="navbarDropdownMenuLinkvideo" role="button" data-bs-toggle="dropdown" aria-expanded="false"
          on:click={() => {
            // $keyword='{"resolution":[],"display_quality":[],"country":[],"face":[],"look":[],"age":[],"pussy":[],"etc":""}',
            // $page=0
            }}>
          동영상</a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLinkvideo">
            <li>
              <a use:link class="dropdown-item" href="/video" 
                  on:click={() => {
                  $keyword='{"resolution":[],"display_quality":[],"country":[],"face":[],"look":[],"age":[],"pussy":[],"etc":""}',
                  $page=0
                  }}>
                all</a>
            </li>
            <li><a use:link class="dropdown-item" href="/video"
                   on:click={() => {
                    $keyword='{"resolution":[],"display_quality":[],"country":[],"face":[],"look":[],"age":[],"pussy":[],"etc":"","vote":true}'
                    $page=0
                    }}
                >
                추천</a></li>
            <li><a use:link class="dropdown-item" href="/video"
                   on:click={() => {
                     $keyword='{"resolution":[],"display_quality":[],"country":[],"face":[],"look":[],"age":[],"pussy":[],"etc":"test2"}',
                     $page=0
                   }}>
                test2</a></li>
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
  .navbar {
  }
  .container {
    display: flex;
    justify-items: flex-end;
    justify-content: flex-end;
  }
  .dropdown-item {
    justify-self: flex-end;
  }
</style>