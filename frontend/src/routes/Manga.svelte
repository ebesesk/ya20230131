<script>
  import fastapi from "../lib/api";
//   import { link } from 'svelte-spa-router'
  import { page } from "../lib/store"
  
  let manga_list = []
  let size = 6
  // let page = 0
  let total = 0
  $: total_page = Math.ceil(total/size)    
  
  
function get_mangas_list(_page) {
  let params = {
    page: _page,
    size: size,
  }
  fastapi('get', '/api/manga/list', params, (json) => {
    manga_list = json.manga_list
    total = json.total
    $page = _page
    console.log(manga_list)
  })
}
    
  function refresh() {
    fastapi ('get', '/api/manga/refresh',  {}, (json) => {
      manga_new = json.new
    })
  }
    
  get_mangas_list(0)
    






// kddddds://http://bbbb/tumblr_ogugfiopri1ve0iel.mp4
</script>
<div class="menu title">
  <button on:click={refresh} class="button refresh">refresh</button>
</div>
<div class="container my-2 " style="width: 100%; height: 100%; ">
  <!-- 페이징처리 시작 -->
  <ul class="pagination justify-content-center">
    <!-- 이전페이지 -->
    <li class="page-item {$page <= 0 && 'disabled'}">
      <button class="page-link" on:click="{() => get_mangas_list($page-1)}"  style="font-size: smaller;">이전</button>
    </li>
    <!-- 페이지번호 -->
    {#each Array(total_page) as _, loop_page}
    {#if loop_page >= $page-5 && loop_page <= $page+5}
    <li class="page-item {loop_page === $page && 'active'}">
      <button on:click="{() => get_mangas_list(loop_page)}" class="page-link"  style="font-size: smaller;">{loop_page+1}</button>
    </li>
    {/if}
    {/each}
    <!-- 다음페이지 -->
    <li class="page-item {$page >= total_page-1 && 'disabled'}">
      <button class="page-link" on:click="{() => get_mangas_list($page+1)}"  style="font-size: smaller;">다음</button>
    </li>
  </ul>
  <!-- 페이징처리 끝 -->
    


<div class="row" style="float: none; margin:100 auto;">
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
    </div>
    <a href="{'kddddds2://http://' + manga.title}" class="caption display-7" 
              style="font-size:smaller; white-space: normal; word-break: break-all;">
              # {manga.title}</a>
    <span class="description">#{manga['images'].length}P</span>
  </div>
  {/each}
</div>






  <!-- <div class="row" style="float: none; margin:100 auto;">
    {#each manga_list as manga, i}
    <div class="col-xxl-2 col-xl-3 col-lg-4 col-sm-6">
      <div class="img-container">
        <img src="{encodeURIComponent(manga['images'][0])}" 
          alt="" class="img-thumbnail img-responsive" 
          style="object-fit: scale-down;">
          <div class="overlay">
            <a href="{'kddddds2://http://' + manga.title}" class="caption display-7" 
              style="font-size:smaller; white-space: normal; word-break: break-all;">
              {manga.title}</a>
          </div>
      </div>
    </div>
    {/each}
  </div> -->




    
  <!-- 페이징처리 시작 -->
  <ul class="pagination justify-content-center">
    <!-- 이전페이지 -->
    <li class="page-item {$page <= 0 && 'disabled'}">
      <button class="page-link" on:click="{() => get_mangas_list($page-1)}" style="font-size: smaller;">이전</button>
    </li>
    <!-- 페이지번호 -->
    {#each Array(total_page) as _, loop_page}
    {#if loop_page >= $page-5 && loop_page <= $page+5}
    <li class="page-item {loop_page === $page && 'active'}">
      <button on:click="{() => get_mangas_list(loop_page)}" class="page-link" style="font-size: smaller;">{loop_page+1}</button>
    </li>
    {/if}
    {/each}
    <!-- 다음페이지 -->
    <li class="page-item {$page >= total_page-1 && 'disabled'}">
      <button class="page-link" on:click="{() => get_mangas_list($page+1)}" style="font-size: smaller;">다음</button>
    </li>
  </ul>

</div>
<style>
    body {
        background-color: black;
    }
    .menu.title {
        text-align: end;
    }
    .button.refresh {
        font-size: smaller;
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
</style>