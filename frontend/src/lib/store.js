import { writable } from 'svelte/store'

const persist_storage = (key, initValue) => {
    const storedValueStr = localStorage.getItem(key)
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
    store.subscribe((val) => {
        localStorage.setItem(key, JSON.stringify(val))
    })
    return store
}

export const page = persist_storage("page", 0)
export const pagev = persist_storage("page", 0)
export const access_token = persist_storage("access_token", 0)
export const username = persist_storage("username", 0)
export const is_login = persist_storage("is_login", 0)
export const keyword = persist_storage("keyword", "")
export const mangaKeyword = persist_storage("mangaKeyword", "")
export const mangaPage = persist_storage("mangaPage", 0)
export const workedKeywords = persist_storage("workedKeywords", ['모산', '최부장'])