<script>
  import fastapi from "../../lib/api";
  //   import { link } from 'svelte-spa-router'
  import { mangaPage, mangaKeyword } from "../../lib/store"
  import Modal from "../../components/Modal.svelte"
  
  let manga_list = []
  // let manga
  let size = 18
  let total = 0
  let modal_search
  let searchValue = ''
  let vote = false
  
  
  $: total_page = Math.ceil(total/size)    
  $: $mangaPage, $mangaKeyword, search()
  search()
  
  function refresh() {
    fastapi ('get', '/api/manga/refresh',  {}, (json) => {
      manga_new = json.new
    })
  }
  
  
  function vote_manga(_manga_id) {
    let url = "/api/manga/vote"
    let params = {
      manga_id: _manga_id
    }
    fastapi('post', url, params,
    (json) => {
      search()
    },
    (err_json) => {
      error = err_json
    }
    )
  }
    
  
  function onVote () {
    vote = true
    search()
  }
  
    
  function search() {
    let params = {
      page: $mangaPage,
      size: size,
      keyword: $mangaKeyword,
      vote: vote
    }
    fastapi('get', '/api/manga/search', params, (json) => {
      manga_list = json.manga_list
      total = json.total
      console.log(total)
    })
  }
  
  
  function onSearch () {
    vote = false
    $mangaPage = 0
    $mangaKeyword = searchValue
    console.log('$mangaPage: ',$mangaPage, 'mangaKeyword: ', $mangaKeyword)
  }
  
  function closemodal() {
    modal_search.hide()
  }
  
// function get_mangas_list(_page) {
//   let params = {
//     page: _page,
//     size: size,
//   }
//   fastapi('get', '/api/manga/list', params, (json) => {
//     manga_list = json.manga_list
//     total = json.total
//     $mangaPage = _page
//     // console.log(manga_list)
//   })
// }

</script>

<div >
  <div class="header-button">
    <button on:click={refresh} class="button refresh">refresh</button>
    <button class="btn btn-sm" on:click={modal_search.show()}>modal show</button>
    
    <!-- 추천보기 -->
    <button class="btn btn-sm" on:click={onVote}>추천보기</button>
    <!-- 검색 -->
    <form on:submit|preventDefault={onSearch}>
      <input type="text" bind:value={searchValue} placeholder="검색"/>
      <button on:click={onsearch}>검색</button>
    </form>
    
  </div>
  <div class="container my-2 " style="width: 100%; height: 100%; ">
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center" style="font-size: smaller;">
      <!-- 이전페이지 -->
      <li class="page-item {$mangaPage <= 0 && 'disabled'}">
        <button class="page-link" on:click="{() => $mangaPage--}"  style="font-size: smaller;">이전</button>
      </li>
      <!-- 페이지번호 -->
      {#each Array(total_page) as _, loop_page}
      {#if loop_page >= $mangaPage-5 && loop_page <= $mangaPage+5}
      <!-- <li class="page-item {loop_page === $mangaPage && 'active'}"> -->
        <li class="page-item ">
          <button on:click="{() => $mangaPage = loop_page}" class="page-link {(loop_page === $mangaPage) && 'font-weight-bol text-danger'}"  style="font-size: smaller;">{loop_page+1}</button>
        </li>
        {/if}
      {/each}
      <!-- 다음페이지 -->
      <li class="page-item {$mangaPage >= total_page-1 && 'disabled'}">
        <button class="page-link" on:click="{() => $mangaPage++}"  style="font-size: smaller;">다음</button>
      </li>
    </ul>
    <!-- 페이징처리 끝 -->
  </div>


  <!-- <div class="row" style="float: none; margin:100 auto;">
    {#each manga_list as manga, i}
    <div class="col-xxl-4 col-xl-4 col-lg-4 col-sm-6">
      
      <div id="manga{i}" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          {#each manga['images'].slice(0,20) as image}
          <div class="carousel-item active">
            <img src="{encodeURIComponent(image)}" class="d-block w-100" alt="...">
          </div>
          {/each}
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#manga{i}" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#manga{i}" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div> -->


      <!-- 추천게시물 -->
      <!-- {#if manga.voter.length > 0}
      <button class="btn btn-sm btn-outline-secondary" on:click={vote_manga(manga['id'])}>
        <span class="badge rounded-pill bg-danger">{manga.voter.length}</span>
      </button>
      {:else}
      <button class="btn btn-sm btn-outline-secondary" on:click={vote_manga(manga['id'])}>
        추천
      </button>
      {/if}
      <a href="{'kddddds2://http://' + manga.title}" class="caption display-7" 
                style="font-size:smaller; white-space: normal; word-break: break-all;">
                # {manga.title}</a>
      <span class="description">#{manga['images'].length}P</span>
    </div>
    {/each}
  </div> -->






  <div class="row" style="float: none; margin:100 auto;">
    {#each manga_list as manga, i}
    <div class="col-xxl-2 col-xl-3 col-lg-4 col-sm-6">
      <div class="img-container">
        <img src="{encodeURIComponent(manga['images'][0])}" 
          alt="{manga['title']}" class="img-thumbnail img-responsive" 
          style="object-fit: scale-down;">
          <div class="overlay">
            <!-- 추천게시물 -->
            {#if manga.voter.length > 0}
            <button class="btn btn-sm btn-outline-secondary" on:click={vote_manga(manga['id'])}>
              <span class="badge rounded-pill bg-danger">{manga.voter.length}</span>
            </button>
            {:else}
            <button class="btn btn-sm btn-outline-secondary" on:click={vote_manga(manga['id'])}>
              추천
            </button>
            {/if}


            
            
            <a href="{'kddddds2://http://' + manga.title}" class="caption display-7" 
              style="font-size:smaller; white-space: normal; word-break: break-all;">
              {manga.title}</a>
              <span class="description">#{manga['images'].length}P</span>
          </div>
      </div>
    </div>
    {/each}
  </div>




  <div>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center" style="font-size: smaller;">
      <!-- 이전페이지 -->
      <li class="page-item {$mangaPage <= 0 && 'disabled'}">
        <button class="page-link" on:click="{() => search($mangaPage-1)}"  style="font-size: smaller;">이전</button>
      </li>
      <!-- 페이지번호 -->
      {#each Array(total_page) as _, loop_page}
      {#if loop_page >= $mangaPage-5 && loop_page <= $mangaPage+5}
      <!-- <li class="page-item {loop_page === $mangaPage && 'active'}"> -->
      <li class="page-item ">
        <button on:click="{() => $mangaPage = loop_page}" class="page-link {(loop_page === $mangaPage) && 'font-weight-bol text-danger'}"  style="font-size: smaller;">{loop_page+1}</button>
      </li>
      {/if}
      {/each}
      <!-- 다음페이지 -->
      <li class="page-item {$mangaPage >= total_page-1 && 'disabled'}">
        <button class="page-link" on:click="{() => $mangaPage++}"  style="font-size: smaller;">다음</button>
      </li>
    </ul>
    <!-- 페이징처리 끝 -->
  </div>
</div>


<Modal bind:this={modal_search}>

  <button on:click={modal_search.hide()} style="font-size: smaller;">Close</button>
</Modal>

<style>
    .header-button {
      display: flex;
      justify-content: flex-end;
    }

    .menu.title {
        text-align: end;
    }
    .button.refresh {
        font-size: smaller;
        padding: 10px 16px;
        outline: none;
        border: none;
        cursor: pointer;
        border-right: 1px solid #ffffff;
        background: #ffffff;
        }
    .d-block.w-100 {
        width: 400px;
        height: 600px;
        object-fit: scale-down;
    }
    .description {
        font-size: smaller;
    }
    .btn.btn-sm.btn-outline-secondary {
        font-size: smaller;
        outline: none;
        border: none;
    }
</style>