from typing import Optional,Any, Dict
from pydantic import Field
from beanie import Indexed , Document
from .base_repository import BaseRepository
# from logging import Logger


class ProductFaqRepository(BaseRepository):
    def __init__(self, model):
        super().__init__(model)
    
    async def create(self,data:Dict[str,Any])-> Document:
        try:
            instance = self.model(**data)
            await instance.save()
            return instance
        except Exception as e:
            print(f"Error occured while creating Product faq : -> {e}")
            # logger.error(f"Error occured while creating Product faq : -> {e}")
            raise

    async def get_all_faq(self,skip:int = 0 , limit:int=10, search:str ="",sort:Dict={}) -> list[Document]:
        try:
            query = {}
            if search:
                query["question"] = {"$regex": search, "$options": "i"}
                query["answer"] = {"$regex": search, "$options": "i"}
                faqs = await self.model.find(query).sort(sort).skip(skip).limit(limit).to_list()
                return faqs
            faqs = await self.model.find({}).sort(sort).skip(skip).limit(limit).to_list()
            return faqs
        except Exception as e:
            print(f"Error occured while fetching Product faq : -> {e}")
            # logger.error(f"Error occured while fetching Product faq : -> {e}")
            raise
    
    async def delete_faq(self,id:Optional[str]="", slug:Optional[str] ="") -> bool:
        try:
            if not slug or not id:
                return False
            faq = await self.model.find_one({
                    "$or":[
                        {"_id":id},
                        {"slug":slug}]
                }
            )

            if not faq:
                return False
            await faq.delete()
            return True
        except Exception as e:
            print(f"Error occured while deleting Product faq : -> {e}")
            # logger.error(f"Error occured while deleting Product faq : -> {e}")
            raise

    async def update_faq(self,id:str,data:Dict[str,str]):
        try:
            faq = await self.model.update_one({"_id":id}, {"$set":data})
            return faq
        except Exception as e:
            print(f"Error occured while updating Product faq : -> {e}")
            # logger.error(f"Error occured while updating Product faq : -> {e}")
            raise

        
