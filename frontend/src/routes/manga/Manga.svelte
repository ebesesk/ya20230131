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
  let little = false
  
  
  
  function refresh() {
    fastapi ('get', '/api/manga/refresh',  {}, (json) => {
      manga_new = json.new
    })
  }
  
  
  function voteManga(_manga_id) {
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
  
  function delVoteManga(_manga_id) {
    let url = "/api/manga/delvote"
    let params = {
      manga_id: _manga_id
    }
    fastapi('delete', url, params,
    (json) => {
      search()
    },
    (error_json) => {
      
    }
    )
  }
  
  
  
  function search() {
    let params = {
      size: size,
      vote: vote,
      little: little,
      page: $mangaPage,
      keyword: $mangaKeyword,
    }
    fastapi('get', '/api/manga/search', params, (json) => {
      manga_list = json.manga_list
      total = json.total
      
    })
  }
  
  
  function onSearch () {
    vote = vote
    little = little
    $mangaPage = 0
    $mangaKeyword = searchValue
  }
  function onVote () {
    little = false
    vote = true
    $mangaPage = 0
    $mangaKeyword = ''
    search()
  }
  function onLittle () {
    little = true
    vote = false
    $mangaPage = 0
    $mangaKeyword = ''
    search()
  }
  
  function closemodal() {
    modal_search.hide()
  }
  $: total_page = Math.ceil(total/size)    
  $: $mangaPage, $mangaKeyword, search()
  search()
  
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

<div class="container-xxl">
  <div class="header-button">
    <button on:click={refresh} class="button refresh">refresh</button>
    <button class="btn btn-sm" on:click={modal_search.show()}>modal show</button>
    <!-- 페이지 적은 -->
    <button class="btn btn-sm" on:click={onLittle}>little</button>
    <!-- 추천보기 -->
    <button class="btn btn-sm" on:click={onVote}>추천보기</button>
    
    <form on:submit|preventDefault={onSearch}>
      <label>
        <input type="checkbox" bind:checked={little}>little
      </label>
      <label>
        <input type="checkbox" bind:checked={vote}>추천
      </label>
    <!-- 검색 -->
      <input type="text" bind:value={searchValue} placeholder="검색"/>
      <button on:click={onSearch}>검색</button>
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

  <div class="row" >
    {#each manga_list as manga, i}
    <div class="col-xxl-1 col-xl-2 col-lg-3 col-sm-6">
      <div class="img-container">
        <img src="{encodeURIComponent(manga['images'][0])}" 
          alt="{manga['title']}" class="img-thumbnail" />

          <div class="overlay">
            <p class="description">
            <!-- 추천게시물 -->
            {#if manga.voter.length > 0}
            <button class="btn btn-sm btn-outline-secondary" on:click={delVoteManga(manga['id'])}>
              <span class="badge rounded-pill bg-danger">{manga.voter.length}</span>
            </button>
            {:else}
            <button class="btn btn-sm btn-outline-secondary" on:click={voteManga(manga['id'])}>
              추천
            </button>
            {/if}
              <a href="{'kddddds2://http://' + manga.title}" class="caption display-7" 
                style="font-size:smaller; white-space: normal; word-break: break-all;">
                보기 #{manga['images'].length}</a> {manga.title}
            </p>
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
    .img-container > img {
      top:0;
      left: 0;
      min-width: 100%;
      height: 250px;
      object-fit: scale-down;
    }
    .header-button {
      display: flex;
      justify-content: flex-end;
      font-size: smaller;
      /* line-height: 100%; */
      align-items: center;

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
    .btn.btn-sm.btn-outline-secondary {
      font-size: smaller;
      outline: none;
      border: none;
    }
    .overlay {
      font-size: smaller;
      /* white-space: nowrap; */
    }
    p.description {
      /* display: flex;   */
      font-size: smaller;
      line-height: 1.3;
    }
</style>