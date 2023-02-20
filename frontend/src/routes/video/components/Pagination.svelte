<script>
  import { page } from "../../../lib/store"

  export let total
  export let size
  $: total_page = Math.ceil(total/size)    

</script>

<!-- 페이징처리 시작 -->
<ul class="pagination justify-content-center" style="font-size: smaller;">
    <!-- 이전페이지 -->
    <li class="page-item {$page <= 0 && 'disabled'}">
      <button class="page-link" on:click="{() => $page--}"  style="font-size: smaller;">이전</button>
    </li>
    <!-- 페이지번호 -->
    {#each Array(total_page) as _, loop_page}
    {#if loop_page >= $page-5 && loop_page <= $page+5}
          
    <!-- <li class="page-item {(loop_page === $page && videoinfo_modal) &&  'active'}"> -->
    <li class="page-item ">
      <button on:click="{() => $page = loop_page}" 
              class="page-link {(loop_page === $page) && 'font-weight-bol text-danger'}"  
              style="font-size: smaller;">
        {(loop_page+1).toString().padStart(3, ' ')}
      </button>
    </li>
    {/if}
    {/each}
    <!-- 다음페이지 -->
    <li class="page-item {$page >= total_page-1 && 'disabled'}">
      <button class="page-link" on:click="{() => $page++}"  style="font-size: smaller;">다음</button>
    </li>
    <li>
    </li>
  </ul>
  <!-- 페이징처리 끝 -->
